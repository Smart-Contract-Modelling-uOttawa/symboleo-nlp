from app.classes.symboleo_contract import ContractSpec
from app.src.rules.shared.configs import PredicateProcessorConfig
from app.classes.spec.sym_event import SymEvent
from app.classes.spec.symboleo_spec import Proposition
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.p_atoms import PAtomPredicate

# Extracts a SymEvent from a 'Happens' predicate in a targeted norm component
class IGetDefaultEvents:
    def get(self, contract_spec: ContractSpec, config: PredicateProcessorConfig) -> SymEvent:
        raise NotImplementedError()

class DefaultEventGetter(IGetDefaultEvents):
    def get(self, contract_spec: ContractSpec, config: PredicateProcessorConfig) -> SymEvent:
        # Find the target norm inside the contract spec
        target_norm = contract_spec.__dict__[config.norm_type][config.norm_id]

        # Get the component
        component: Proposition = getattr(target_norm, config.norm_component)

        # Get the PAtom
        patom = component.p_ands[0].p_eqs[0].p_comps[0].p_atoms[0]
        
        if isinstance(patom, PAtomPredicate):
            predicate = patom.predicate_function

            if isinstance(predicate, PredicateFunctionHappens):
                return predicate.event

        raise NotImplementedError('Default event not found!')