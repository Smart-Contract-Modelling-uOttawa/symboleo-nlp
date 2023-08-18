from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.domain_updates import DomainUpdates
from app.classes.spec.norm_config import NormConfig
from app.src.domain_update_extractor.declaration_mapper import IMapDeclarations
from app.src.domain_update_extractor.domain_model_mapper import IMapDeclarationToDomain
from app.src.domain_update_extractor.contract_parm_mapper import IMapContractParms

class IExtractDomainUpdates:
    def extract(self, pattern_class: PatternClass, contract: SymboleoContract, norm_config: NormConfig) -> DomainUpdates:
        raise NotImplementedError()
    
class DomainUpdateExtractor(IExtractDomainUpdates):
    def __init__(
        self,
        decl_mapper: IMapDeclarations,
        domain_mapper: IMapDeclarationToDomain,
        contract_parm_mapper: IMapContractParms
    ):
        self.__decl_mapper = decl_mapper
        self.__domain_mapper = domain_mapper
        self.__contract_parm_extractor = contract_parm_mapper
    
    def extract(self, pattern_class: PatternClass, contract: SymboleoContract, norm_config: NormConfig) -> DomainUpdates:
        declarations = self.__decl_mapper.map(pattern_class, contract, norm_config)
        domain_objects = [self.__domain_mapper.map(x) for x in declarations]
        contract_parms = self.__contract_parm_extractor.map(pattern_class, norm_config)
        return DomainUpdates(declarations, domain_objects, contract_parms)
        
