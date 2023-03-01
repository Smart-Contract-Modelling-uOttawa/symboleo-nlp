from app.classes.spec.helpers import VariableDotExpression
from app.classes.spec.power_function import PowerFunction
from app.classes.spec.proposition import Proposition
# XText link: https://github.com/Smart-Contract-Modelling-uOttawa/Symboleo-IDE/blob/master/ca.uottawa.csmlab.symboleo/src/ca/uottawa/csmlab/symboleo/Symboleo.xtext


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
