from enum import Enum
from typing import List
from app.classes.spec.power_function import PowerFunction
from app.classes.spec.proposition import Proposition, PNegAtom, PAnd, PEquality, PComparison
from app.classes.spec.p_atoms import PAtomPredicate, PAtomPredicateFalseLiteral, PAtomPredicateTrueLiteral
from app.classes.spec.predicate_function import PredicateFunction, PredicateFunctionHappens
from app.src.operations.parm_configs import ParmOpCode
# XText link: https://github.com/Smart-Contract-Modelling-uOttawa/Symboleo-IDE/blob/master/ca.uottawa.csmlab.symboleo/src/ca/uottawa/csmlab/symboleo/Symboleo.xtext

class NormType(Enum):
    Obligation = 'Obligation'
    Power = 'Power'
    SurvivingObligation = 'SO'


class INorm:
    def update(self, str_component: str, predicate: PredicateFunction):
        raise NotImplementedError()
    def get_default_event(self, str_component:str):
        raise NotImplementedError()
    def get_negation(self, str_component: str) -> bool:
        raise NotImplementedError()
    def get_op_codes(self) -> List[ParmOpCode]:
        raise NotImplementedError()
    def to_sym(self):
        raise NotImplementedError()
    

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
    

    def update(self, str_component: str, predicate: PredicateFunction):
        negation = self.get_negation(str_component)
        
        new_atom = PNegAtom(PAtomPredicate(predicate), negation)
        new_p_and = PAnd([PEquality(PComparison(new_atom))])

        component: Proposition = getattr(self, str_component)

        # If non-existent, then create it
        if not component or type(component) in [PAtomPredicateTrueLiteral, PAtomPredicateFalseLiteral]:
            component = Proposition(p_ands = [])
            component.p_ands.append(new_p_and)
        
        # If one already exists, then need the PAnd
        else:
            #component.p_ands.append(new_p_and) # Appends;
            component.p_ands = [new_p_and] # Replaces; rather than appends. May need a flag argument...
        
        setattr(self, str_component, component)


    def get_default_event(self, str_component:str):
        component: Proposition = getattr(self, str_component)

        if not component or type(component) in [PAtomPredicateTrueLiteral, PAtomPredicateFalseLiteral]:
            return None

        # Get the PAtom
        p_neg_atom = component.p_ands[0].p_eqs[0].curr.curr        
        if isinstance(p_neg_atom, PNegAtom):
            p_atom = p_neg_atom.atom
            if isinstance (p_atom, PAtomPredicate):
                predicate_function = p_atom.predicate_function
                if isinstance(predicate_function, PredicateFunctionHappens):
                    return predicate_function.event

        raise NotImplementedError('Default event not found!')


    def get_negation(self, str_component: str) -> bool:
        result = False

        component: Proposition = getattr(self, str_component)

        # If its non-empty
        try:
            pneg: PNegAtom = component.p_ands[0].p_eqs[0].curr.curr
            result = pneg.negation 
        except Exception as e:
            result = False

        return result
    
    
    def get_op_codes(self) -> List[ParmOpCode]:
        results = []
        if not self.trigger:
            results.append(ParmOpCode.ADD_TRIGGER)
        
        pneg: PNegAtom = self.consequent.p_ands[0].p_eqs[0].curr.curr
        patom_pred: PAtomPredicate = pneg.atom
        
        if type(patom_pred.predicate_function) == PredicateFunctionHappens:
            results.append(ParmOpCode.REFINE_PREDICATE)

        # TODO: Will eventually need a condition on this...
        results.append(ParmOpCode.ADD_NORM)

        return results


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
