import copy
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.symboleo_contract import SymboleoContract
from app.src.rules.shared.configs import PredicateProcessorConfig
from app.src.rules.contract_spec.norm_proposition_updater import IUpdateNormPropositions
from app.classes.spec.symboleo_spec import PNegAtom
from app.classes.spec.p_atoms import PAtomPredicate

class TbppProcessor:
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
