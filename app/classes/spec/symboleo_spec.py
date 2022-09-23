class Atom:
    def to_sym(self):
        raise NotImplementedError()

class NegAtom:
    def __init__(self, atom: Atom, negation: bool = False):
        self.atom = atom
        self.negation = negation

    def to_sym(self):
        result = self.atom.to_sym()

        if self.negation:
            result = f'NOT {result}'
        
        return result
        

class Junction:
    def __init__(self, negAtoms: list[NegAtom]):
        self.negAtoms = negAtoms
    
    def to_sym(self):
        return ' AND '.join([x.to_sym() for x in self.negAtoms])


class Proposition:
    def __init__(self, junctions: list[Junction]):
        self.junctions = junctions
    
    def to_sym(self):
        return ' OR '.join([x.to_sym() for x in self.junctions])

class Role:
    def __init__(self, name: str):
        self.name = name
    
    def to_sym(self):
        return self.name


class Norm:
    def __init__(
        self,
        id: str,
        trigger: Proposition,
        debtor: Role,
        creditor: Role,
        antecedent: Proposition,
        consequent: Proposition,
        norm_type
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
            trigger_text = self.trigger.to_sym() + ' => '

        deb_text = self.debtor.to_sym()
        cred_text = self.creditor.to_sym()

        ant_text = 'T'
        if self.antecedent:
            ant_text = self.antecedent.to_sym()
        
        con_text = self.consequent.to_sym()

        return f'{self.id}: {trigger_text}{self.norm_type}({deb_text}, {cred_text}, {ant_text}, {con_text})'

class Obligation(Norm):
    def __init__(
        self, 
        id: str, 
        trigger: Proposition, 
        debtor: Role, 
        creditor: Role, 
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
        debtor: Role, 
        creditor: Role, 
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
            'P')
    
    def to_sym(self):
        return super().to_sym()
