from typing import List
from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.spec.declaration import Declaration
from app.classes.spec.domain_object import DomainObject
from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.sym_updaters.custom_event.event_declaration_mapper import IMapEventToDeclaration
from app.src.sym_updaters.custom_event.asset_declaration_mapper import IMapAssetDeclarations
from app.src.sym_updaters.custom_event.domain_model_mapper import IMapDeclarationToDomain

class DomainUpdates:
    def __init__(
        self,
        declarations: List[Declaration],
        domain_objects: List[DomainObject]
    ):
        self.declarations = declarations
        self.domain_objects = domain_objects

class IExtractDomainUpdates:
    def extract(self, pattern: Pattern, contract: SymboleoContract) -> DomainUpdates:
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
    
    def extract(self, pattern: Pattern, contract: SymboleoContract) -> DomainUpdates:
        declarations = []
        domain_objects = []

        if isinstance(pattern, EventPattern) and isinstance(pattern.event, CustomEvent):
            evt = pattern.event

            asset_decls = self.__asset_decl_mapper.map(evt, contract)
            declarations.extend(asset_decls)

            # Might then be passing asset_decls into this
            # Any Noun phrase should be an asset by this point... I think...
            event_decl = self.__event_decl_mapper.map(evt)
            if event_decl:
                declarations.append(event_decl)

            next_dms = [self.__domain_mapper.map(x) for x in declarations]
            domain_objects.extend(next_dms)
        
        return DomainUpdates(declarations, domain_objects)
        