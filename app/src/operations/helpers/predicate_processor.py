import copy
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.symboleo_contract import SymboleoContract
from app.classes.spec.contract_spec import Norm
from app.classes.spec.proposition import PNegAtom, Proposition
from app.classes.spec.p_atoms import PAtomPredicate
from app.src.operations.configs import ParameterConfig
from app.src.operations.helpers.norm_proposition_updater import IUpdateNormPropositions
from app.src.operations.helpers.negation_extractor import IExtractNegations

class IProcessPredicates:
    def process(self, config: ParameterConfig, contract: SymboleoContract, predicate: PredicateFunction) -> SymboleoContract:
        raise NotImplementedError() 


class PredicateProcessor(IProcessPredicates):
    def __init__(
        self,
        negation_extractor: IExtractNegations,
        norm_updater: IUpdateNormPropositions
    ):
        self.__negation_exractor = negation_extractor
        self.__norm_updater = norm_updater


    def process(self, config: ParameterConfig, contract: SymboleoContract, predicate: PredicateFunction) -> SymboleoContract:
        # Get the norm to be updated
        new_spec = copy.deepcopy(contract.contract_spec)
        norm_to_update: Norm = new_spec.__dict__[config.norm_type][config.norm_id]

        negation = self.__negation_exractor.extract(norm_to_update, config.norm_component)
        new_atom = PNegAtom(PAtomPredicate(predicate), negation)

        # Update the norm
        new_norm = self.__norm_updater.update(norm_to_update, config.norm_component, new_atom)
        new_spec.__dict__[config.norm_type][config.norm_id] = new_norm

        # Return the updated Symboleo Contract
        return SymboleoContract(contract.domain_model, new_spec, contract.nl_template)
