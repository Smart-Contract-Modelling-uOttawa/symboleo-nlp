from typing import List
from app.classes.patterns.pattern_classes import PatternClass, EventPatternClass
from app.classes.patterns.all_patterns import *
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.spec.declaration import Declaration
from app.classes.spec.domain_object import DomainObject
from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.domain_update_extractor.event_declaration_mapper import IMapEventToDeclaration
from app.src.domain_update_extractor.asset_declaration_mapper import IMapAssetDeclarations
from app.src.domain_update_extractor.domain_model_mapper import IMapDeclarationToDomain

from app.src.element_extractors.custom_event_extractor import IExtractCustomEvents

# TODO: Move to classes
class DomainUpdates:
    def __init__(
        self,
        declarations: List[Declaration],
        domain_objects: List[DomainObject]
    ):
        self.declarations = declarations
        self.domain_objects = domain_objects

class IExtractDomainUpdates:
    def extract(self, pattern_class: PatternClass, contract: SymboleoContract) -> DomainUpdates:
        raise NotImplementedError()
    
class DomainUpdateExtractor(IExtractDomainUpdates):
    def __init__(
        self,
        asset_decl_mapper: IMapAssetDeclarations,
        event_decl_mapper: IMapEventToDeclaration,
        domain_mapper: IMapDeclarationToDomain
    ):
        self.__asset_decl_mapper = asset_decl_mapper
        self.__event_decl_mapper = event_decl_mapper
        self.__domain_mapper = domain_mapper
    
    def extract(self, pattern_class: PatternClass, contract: SymboleoContract) -> DomainUpdates:
        declarations = []
        domain_objects = []

        if isinstance(pattern_class, EventPatternClass):
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


        # TODO: F3 - For the BEFORE DATE pattern - may want to add event property (e.g. delivery_date)
        ## Would require extracting the initial event declaration - may need to pass in the norm...
        ## And updating the domain event and declaration
        ## Then in the contract updates, would need to merge the new properties. 
        
        return DomainUpdates(declarations, domain_objects)
        