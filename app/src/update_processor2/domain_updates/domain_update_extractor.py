from typing import List
from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.patterns.all_patterns import *
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.spec.declaration import Declaration
from app.classes.spec.domain_object import DomainObject
from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.update_processor.event_declaration_mapper import IMapEventToDeclaration
from app.src.update_processor.asset_declaration_mapper import IMapAssetDeclarations
from app.src.update_processor.domain_model_mapper import IMapDeclarationToDomain

from app.src.update_processor2.domain_updates.custom_event_extractor import IExtractCustomEvents

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
    def extract(self, input_list: List[UserInput], contract: SymboleoContract) -> DomainUpdates:
        raise NotImplementedError()
    
class DomainUpdateExtractor(IExtractDomainUpdates):
    def __init__(
        self,
        asset_decl_mapper: IMapAssetDeclarations,
        event_decl_mapper: IMapEventToDeclaration,
        domain_mapper: IMapDeclarationToDomain,
        custom_event_extractor: IExtractCustomEvents
    ):
        self.__custom_event_extractor = custom_event_extractor
        self.__asset_decl_mapper = asset_decl_mapper
        self.__event_decl_mapper = event_decl_mapper
        self.__domain_mapper = domain_mapper
    
    def extract(self, input_list: List[UserInput], contract: SymboleoContract) -> DomainUpdates:
        declarations = []
        domain_objects = []

        evt = self.__custom_event_extractor.extract(input_list, contract)
        if evt:
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
        