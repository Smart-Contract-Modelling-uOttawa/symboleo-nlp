from typing import List
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.operations.contract_update_obj import ContractUpdateObj

from app.src.pattern_builder.pattern_class_builder import IBuildPatternClass
from app.src.operations.pattern_class_resolver import IResolvePatternClasses
from app.src.norm_update_extractor.norm_update_extractor import IExtractNormUpdates
from app.src.domain_update_extractor.domain_update_extractor import IExtractDomainUpdates
from app.classes.pattern_classes.before_date import BeforeDate

class IMapCnlToOperations:
    def map(self, input_list: List[UserInput], contract: SymboleoContract, norm_config: NormConfig) -> ContractUpdateObj:
        raise NotImplementedError()

class OperationMapper(IMapCnlToOperations):
    def __init__(
        self,
        pattern_class_builder: IBuildPatternClass,
        pattern_class_resolver: IResolvePatternClasses,
        norm_update_extractor: IExtractNormUpdates,
        domain_update_extractor: IExtractDomainUpdates
    ):
        self.__pattern_class_builder = pattern_class_builder
        self.__pattern_class_resolver = pattern_class_resolver
        self.__norm_update_extractor = norm_update_extractor
        self.__domain_update_extractor = domain_update_extractor


    def map(self, input_list: List[UserInput], contract: SymboleoContract, norm_config:NormConfig) -> ContractUpdateObj:
        pattern_classes = self.__pattern_class_builder.build(input_list, contract)
        
        pattern_class = self.__pattern_class_resolver.resolve(pattern_classes, norm_config)

        norms = self.__norm_update_extractor.extract(pattern_class, norm_config)

        domain_updates = self.__domain_update_extractor.extract(pattern_class, contract)

        nl_update = pattern_class.to_text()
        
        return ContractUpdateObj(
            norms, 
            domain_updates.domain_objects, 
            domain_updates.declarations,
            domain_updates.contract_parms, 
            nl_update
        )
        