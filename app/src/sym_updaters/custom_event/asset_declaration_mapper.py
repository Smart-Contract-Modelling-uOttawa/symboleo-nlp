from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_object import Asset
from app.classes.spec.declaration import AssetDeclaration
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.custom_event.noun_phrase import NounPhrase

from app.src.sym_updaters.custom_event.asset_decl_extractor import IExtractAssetDeclarations

# Look through the CustomEvent at the noun phrases
# For any that are not roles and not in the asset set, create a new asset
# Might create multiple... subj, dobj, pps...
# This is where we need access to the contract. At the very least we need the assets
# MAy want to just return ALL assets, as that may be useful in the subsequent declaration_mapper call
## It will need to know about any new assets that have been created...
class IMapAssetDeclarations:
    def map(self, custom_event: CustomEvent, contract: SymboleoContract) -> List[AssetDeclaration]:
        raise NotImplementedError()

class AssetDeclarationMapper(IMapAssetDeclarations):
    def __init__(self, asset_extractor: IExtractAssetDeclarations):
        self.__asset_extractor = asset_extractor # May not need this.

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
    
    
    
