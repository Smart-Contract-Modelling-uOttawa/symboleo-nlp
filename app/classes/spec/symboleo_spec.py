from app.classes.spec.helpers import VariableDotExpression
from app.classes.spec.power_function import PowerFunction

class PAtom:
    def to_sym(self):
        raise NotImplementedError()
        
class PComparison:
    def __init__(self, p_atoms: list[PAtom], op: str = ''):
        self.p_atoms = p_atoms
        self.op = op # ">=" | "<=" | ">" | "<"
    
    def to_sym(self):
        return f' {self.op} '.join([x.to_sym() for x in self.p_atoms])


class PEquality:
    def __init__(self, p_comps: list[PComparison], op: str = ''):
        self.p_comps = p_comps
        self.op = op # == or !=
    
    def to_sym(self):
        return f' {self.op} '.join([x.to_sym() for x in self.p_comps])

# TODO: May not need this... already have an 'AND' joiner... May need an OR joiner...
class PAnd:
    def __init__(self, p_eqs: list[PEquality]):
        self.p_eqs = p_eqs
    
    def to_sym(self):
        return ' AND '.join([x.to_sym() for x in self.p_eqs])

class Proposition:
    def __init__(self, p_ands: list[PAnd]):
        self.p_ands = p_ands
    
    def to_sym(self):
        return ' AND '.join([x.to_sym() for x in self.p_ands])


class Norm:
    def __init__(
        self,
        id: str,
        trigger: Proposition,
        debtor: VariableDotExpression,
        creditor: VariableDotExpression,
        antecedent: Proposition,
        consequent: Proposition,
        norm_type: str
    ):
        self.id = id
        self.trigger = trigger
        self.debtor = debtor
        self.creditor = creditor
        self.antecedent = antecedent
        self.consequent = consequent
        self.norm_type = norm_type # O or P
    
    def to_sym(self):
        trigger_text = ''
        if self.trigger:
            trigger_text = self.trigger.to_sym() + ' -> '

        deb_text = self.debtor.to_sym()
        cred_text = self.creditor.to_sym()

        ant_text = 'true'
        if self.antecedent:
            ant_text = self.antecedent.to_sym()
        
        con_text = self.consequent.to_sym()

        return f'{self.id}: {trigger_text}{self.norm_type}({deb_text}, {cred_text}, {ant_text}, {con_text})'

class Obligation(Norm):
    def __init__(
        self, 
        id: str, 
        trigger: Proposition, 
        debtor: VariableDotExpression, 
        creditor: VariableDotExpression, 
        antecedent: Proposition, 
        consequent: Proposition
    ):
        super().__init__(
            id, 
            trigger, 
            debtor, 
            creditor, 
            antecedent, 
            consequent, 
            'O')
    
    def to_sym(self):
        return super().to_sym()


class Power(Norm):
    def __init__(
        self, 
        id: str, 
        trigger: Proposition, 
        debtor: VariableDotExpression, 
        creditor: VariableDotExpression, 
        antecedent: Proposition, 
        consequent: PowerFunction
    ):
        super().__init__(
            id, 
            trigger, 
            debtor, 
            creditor, 
            antecedent, 
            None, 
            'P')
        self.consequent = consequent 
    
    def to_sym(self):
        return super().to_sym()
