from typing import List
from app.classes.spec.norm import Norm
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.operations.contract_update_obj import ContractUpdateObj

from app.classes.operations.handle_object import HandleObject

from app.src.pattern_builder.pattern_class_builder import IBuildPatternClass
from app.src.norm_update_extractor.norm_update_extractor import IExtractNormUpdates
from app.src.domain_update_extractor.domain_update_extractor import IExtractDomainUpdates

class IMapCnlToOperations:
    def map(self, input_list: List[UserInput], contract: SymboleoContract, norm: Norm) -> ContractUpdateObj:
        raise NotImplementedError()

class OperationMapper(IMapCnlToOperations):
    def __init__(
        self,
        pattern_class_builder: IBuildPatternClass,
        norm_update_extractor: IExtractNormUpdates,
        domain_update_extractor: IExtractDomainUpdates
    ):
        self.__pattern_class_builder = pattern_class_builder
        self.__norm_update_extractor = norm_update_extractor
        self.__domain_update_extractor = domain_update_extractor


    def map(self, input_list: List[UserInput], contract: SymboleoContract, norm:Norm) -> ContractUpdateObj:
        pattern_class = self.__pattern_class_builder.build(input_list, contract)

        handle_object = HandleObject(norm)

        norms = self.__norm_update_extractor.extract(pattern_class, handle_object)

        domain_updates = self.__domain_update_extractor.extract(input_list, contract)

        nl_update = pattern_class.to_text()
        
        return ContractUpdateObj(norms, domain_updates.domain_objects, domain_updates.declarations, nl_update)
        