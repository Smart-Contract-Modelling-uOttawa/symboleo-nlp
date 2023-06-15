from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.declaration import AssetDeclaration
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.events.custom_event.noun_phrase import NounPhrase

from app.src.update_processor.asset_declaration_extractor import IExtractAssetDeclarations


# TODO: E3 - Clean and break this up
class IMapAssetDeclarations:
    def map(self, custom_event: CustomEvent, contract: SymboleoContract) -> List[AssetDeclaration]:
        raise NotImplementedError()

class AssetDeclarationMapper(IMapAssetDeclarations):
    def __init__(self, asset_extractor: IExtractAssetDeclarations):
        self.__asset_extractor = asset_extractor 

    def map(self, custom_event: CustomEvent, contract: SymboleoContract) -> List[AssetDeclaration]:
        results = []

        # These are types that we do NOT want to add on to the existing contract
        exclusions = ['Role', 'Date', 'Contract', 'Money']
        exclusions.extend([x.name for x in contract.domain_model.enums])

        if self._should_include(custom_event.subj, exclusions):
            next_asset = self.__asset_extractor.extract(custom_event.subj)
            results.append(next_asset)
        
        if custom_event.dobj and self._should_include(custom_event.dobj, exclusions):
            next_asset = self.__asset_extractor.extract(custom_event.dobj)
            results.append(next_asset)

        pps = custom_event.pps
        if pps:
            for pp in pps:
                if self._should_include(pp.pobj, exclusions):
                    next_asset = self.__asset_extractor.extract(pp.pobj)
                    results.append(next_asset)
        
        return results


    def _should_include(self, np: NounPhrase, exclusions: List[str]):
        return np.asset_type not in exclusions
    
    
    
