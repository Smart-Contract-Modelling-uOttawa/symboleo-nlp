from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.domain_updates import DomainUpdates
from app.src.domain_update_extractor.event_declaration_mapper import IMapEventToDeclaration
from app.src.domain_update_extractor.asset_declaration_mapper import IMapAssetDeclarations
from app.src.domain_update_extractor.domain_model_mapper import IMapDeclarationToDomain
from app.src.domain_update_extractor.contract_parm_mapper import IMapContractParms

class IExtractDomainUpdates:
    def extract(self, pattern_class: PatternClass, contract: SymboleoContract) -> DomainUpdates:
        raise NotImplementedError()
    
class DomainUpdateExtractor(IExtractDomainUpdates):
    def __init__(
        self,
        asset_decl_mapper: IMapAssetDeclarations,
        event_decl_mapper: IMapEventToDeclaration,
        domain_mapper: IMapDeclarationToDomain,
        contract_parm_mapper: IMapContractParms
    ):
        self.__asset_decl_mapper = asset_decl_mapper
        self.__event_decl_mapper = event_decl_mapper
        self.__domain_mapper = domain_mapper
        self.__contract_parm_extractor = contract_parm_mapper
    
    def extract(self, pattern_class: PatternClass, contract: SymboleoContract) -> DomainUpdates:
        declarations = []
        domain_objects = []

        if isinstance(pattern_class, EventPatternClass) and pattern_class.nl_event.is_new:
            evt = pattern_class.nl_event
            asset_decls = self.__asset_decl_mapper.map(evt, contract)
            declarations.extend(asset_decls)

            # for x in asset_decls:
            #     x.print_me()

            event_decl = self.__event_decl_mapper.map(evt)
            if event_decl:
                declarations.append(event_decl)

            next_dms = [self.__domain_mapper.map(x) for x in declarations]
            domain_objects.extend(next_dms)
        
        contract_parms = self.__contract_parm_extractor.map(pattern_class)


        # TODO: F3 - For the BEFORE DATE pattern - may want to add event property (e.g. delivery_date)
        ## Would require extracting the initial event declaration - may need to pass in the norm...
        ## And updating the domain event and declaration
        ## Then in the contract updates, would need to merge the new properties. 
        
        return DomainUpdates(declarations, domain_objects, contract_parms)
        