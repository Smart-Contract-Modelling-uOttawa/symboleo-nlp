from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.declaration import Declaration
from app.classes.spec.norm_config import NormConfig

from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass

from app.src.domain_update_extractor.asset_declaration_mapper import IMapAssetDeclarations
from app.src.domain_update_extractor.event_declaration_mapper import IMapEventToDeclaration


class IMapDeclarations:
    def map(self, pattern_class: PatternClass, contract: SymboleoContract, norm_config: NormConfig) -> List[Declaration]:
        raise NotImplementedError()

class DeclarationMapper(IMapDeclarations):
    def __init__(
        self, 
        asset_decl_mapper: IMapAssetDeclarations,
        event_decl_mapper: IMapEventToDeclaration
    ):
        self.__asset_mapper = asset_decl_mapper
        self.__event_mapper = event_decl_mapper

    def map(self, pattern_class: PatternClass, contract: SymboleoContract, norm_config: NormConfig) -> List[Declaration]:
        results = []

        if isinstance(pattern_class, EventPatternClass) and pattern_class.nl_event.is_new:
            evt = pattern_class.nl_event
            asset_decls = self.__asset_mapper.map(evt, contract)
            results.extend(asset_decls)

            # for x in asset_decls:
            #     x.print_me()

            event_decl = self.__event_mapper.map(evt)
            if event_decl:
                results.append(event_decl)            

        return results


    
    
