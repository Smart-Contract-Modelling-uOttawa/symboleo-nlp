from enum import Enum
from app.classes.spec.power_function import PowerFunction
from app.classes.spec.proposition import Proposition
# XText link: https://github.com/Smart-Contract-Modelling-uOttawa/Symboleo-IDE/blob/master/ca.uottawa.csmlab.symboleo/src/ca/uottawa/csmlab/symboleo/Symboleo.xtext

class NormType(Enum):
    Obligation = 'Obligation'
    Power = 'Power'
    SurvivingObligation = 'SO'


class Norm:
    def __init__(
        self,
        id: str,
        trigger: Proposition,
        debtor: str,
        creditor: str,
        antecedent: Proposition,
        consequent: Proposition,
        norm_type: NormType
    ):
        self.id = id
        self.trigger = trigger
        self.debtor = debtor
        self.creditor = creditor
        self.antecedent = antecedent
        self.consequent = consequent
        self.norm_type = norm_type
    
    def to_sym(self):
        trigger_text = ''
        if self.trigger:
            trigger_text = self.trigger.to_sym() + ' -> '

        deb_text = self.debtor
        cred_text = self.creditor
        ant_text = self.antecedent.to_sym()        
        con_text = self.consequent.to_sym()

        return f'{self.id}: {trigger_text}{self.norm_type.value}({deb_text}, {cred_text}, {ant_text}, {con_text});'

class Obligation(Norm):
    def __init__(
        self, 
        id: str, 
        trigger: Proposition, 
        debtor: str, 
        creditor: str, 
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
            NormType.Obligation)
    
    def to_sym(self):
        return super().to_sym()


class Power(Norm):
    def __init__(
        self, 
        id: str, 
        trigger: Proposition, 
        debtor: str, 
        creditor: str, 
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
            NormType.Power)
        self.consequent = consequent 
    
    def to_sym(self):
        return super().to_sym()
