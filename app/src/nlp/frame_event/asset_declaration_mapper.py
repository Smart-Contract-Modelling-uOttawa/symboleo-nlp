from typing import List
from app.classes.spec.domain_object import Asset
from app.classes.spec.declaration import Declaration
from app.classes.other.frame_event import FrameEvent
from app.classes.other.noun_phrase import NounPhrase

from app.src.nlp.frame_event.asset_decl_extractor import IExtractAssetDeclarations

# Look through the CustomEvent at the noun phrases
# For any that are not roles and not in the asset set, create a new asset
# Might create multiple... subj, dobj, pps...
# This is where we need access to the contract. At the very least we need the assets
# MAy want to just return ALL assets, as that may be useful in the subsequent declaration_mapper call
## It will need to know about any new assets that have been created...
class IMapAssetDeclarations:
    def map(self, frame_event: FrameEvent, asset_decls: List[Declaration] = None) -> List[Declaration]:
        raise NotImplementedError()

class AssetDeclarationMapper(IMapAssetDeclarations):
    def __init__(self, asset_extractor: IExtractAssetDeclarations):
        self.__asset_extractor = asset_extractor

    def map(self, frame_event: FrameEvent, asset_decls: List[Declaration] = None) -> List[Asset]:
        results = []
        self.__asset_decls = asset_decls

        if not frame_event.subj.is_role and not self._is_decl(frame_event.subj):
            next_asset = self.__asset_extractor.extract(frame_event.subj)
            results.append(next_asset)

        dobj = frame_event.dobj
        if dobj and not dobj.is_role and not self._is_decl(dobj):
            next_asset = self.__asset_extractor.extract(dobj)
            results.append(next_asset)
        
        pps = frame_event.pps
        if pps:
            for pp in pps:
                if not pp.pobj.is_role and not self._is_decl(pp.pobj):
                    next_asset = self.__asset_extractor.extract(pp.pobj)
                    results.append(next_asset)
        
        return results


    def _is_decl(self, np: NounPhrase):
        if not self.__asset_decls:
            return False
        
        # Will it be str_val or to_text...?
        ## If we're choosing from a list of options, then probably str_val...
        if np.str_val in [x.name for x in self.__asset_decls]:
            return True
        else:
            return False
    
    
