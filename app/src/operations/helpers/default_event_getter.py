from app.classes.symboleo_contract import ContractSpec
from app.src.operations.configs import ParameterConfig
from app.classes.spec.sym_event import SymEvent
from app.classes.spec.proposition import Proposition, PNegAtom
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.p_atoms import PAtomPredicate, PAtom
from app.classes.spec.p_atoms import PAtomPredicateFalseLiteral, PAtomPredicateTrueLiteral

# Extracts a SymEvent from a 'Happens' predicate in a targeted norm component
class IGetDefaultEvents:
    def get(self, contract_spec: ContractSpec, config: ParameterConfig) -> SymEvent:
        raise NotImplementedError()

class DefaultEventGetter(IGetDefaultEvents):
    def get(self, contract_spec: ContractSpec, config: ParameterConfig) -> SymEvent:
        # Find the target norm inside the contract spec
        target_norm = contract_spec.__dict__[config.norm_type][config.norm_id]

        # Get the component
        component: Proposition = getattr(target_norm, config.norm_component)

        # If we're dealing with an empty proposition, then there is no default event
        ## Maybe only the case if the norm_component is trigger or antecedent?
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