import copy
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.symboleo_contract import SymboleoContract
from app.classes.spec.proposition import PNegAtom
from app.classes.spec.p_atoms import PAtomPredicate
from app.src.operations.configs import PredicateProcessorConfig
from app.src.operations.helpers.norm_proposition_updater import IUpdateNormPropositions

class IProcessPredicates:
    def process(self, config: PredicateProcessorConfig, contract: SymboleoContract, predicate: PredicateFunction) -> SymboleoContract:
        raise NotImplementedError() 


class PredicateProcessor(IProcessPredicates):
    def __init__(
        self,
        norm_updater: IUpdateNormPropositions
    ):
        self.__norm_updater = norm_updater


    def process(self, config: PredicateProcessorConfig, contract: SymboleoContract, predicate: PredicateFunction) -> SymboleoContract:
        # Get the norm to be updated
        new_spec = copy.deepcopy(contract.contract_spec)
        norm_to_update = new_spec.__dict__[config.norm_type][config.norm_id]
        new_atom = PNegAtom(PAtomPredicate(predicate), False)

        # Update the norm
        new_norm = self.__norm_updater.update(norm_to_update, config.norm_component, new_atom)
        new_spec.__dict__[config.norm_type][config.norm_id] = new_norm

        # Return the updated Symboleo Contract
        return SymboleoContract(contract.domain_model, new_spec, contract.template_strings)