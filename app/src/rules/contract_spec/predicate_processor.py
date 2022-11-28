import copy
from app.src.rules.shared.interfaces import IProcessDocs, IExtractPredicates
from app.src.rules.shared.configs import PredicateProcessorConfig
from app.classes.symboleo_contract import SymboleoContract
from app.src.rules.shared.interfaces import IExtractPredicates
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.norm_proposition_updater import IUpdateNormPropositions
from app.classes.spec.symboleo_spec import PNegAtom
from app.classes.spec.p_atoms import PAtomPredicate

class PredicateProcessor(IProcessDocs):
    def __init__(
        self,
        config: PredicateProcessorConfig,
        predicate_extractor: IExtractPredicates,
        norm_updater: IUpdateNormPropositions
    ):
        self.__config = config
        self.__predicate_extractor = predicate_extractor
        self.__norm_updater = norm_updater

    def process(self, req: ContractUpdateRequest) -> SymboleoContract:
        # Get the norm to be updated
        new_spec = copy.deepcopy(req.contract.contract_spec)
        norm_to_update = new_spec.__dict__[self.__config.norm_type][self.__config.norm_id]

        # Extract the new atom
        new_predicate = self.__predicate_extractor.extract(req)
        new_atom = PNegAtom(PAtomPredicate(new_predicate), False)

        # Update the norm
        new_norm = self.__norm_updater.update(norm_to_update, self.__config.norm_component, new_atom)
        new_spec.__dict__[self.__config.norm_type][self.__config.norm_id] = new_norm

        return SymboleoContract(req.contract.domain_model, new_spec, req.contract.template_strings)
