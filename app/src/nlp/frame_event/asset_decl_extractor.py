from app.classes.spec.domain_object import Asset
from app.classes.spec.declaration import Declaration
from app.classes.other.frame_event import FrameEvent
from app.classes.other.noun_phrase import NounPhrase
from app.classes.other.noun_phrase import NounPhrase

from app.src.nlp.frame_event.asset_type_extractor import IExtractAssetType

# May want to pass in frame event for more context...
class IExtractAssetDeclarations:
    def extract(self, noun_phrase: NounPhrase) -> Declaration:
        raise NotImplementedError()


class AssetDeclarationExtractor(IExtractAssetDeclarations):
    def __init__(self, asset_type_extractor: IExtractAssetType):
        self.__asset_type_extractor = asset_type_extractor

    def extract(self, noun_phrase: NounPhrase) -> Declaration:
        # default case
        txt = noun_phrase.to_text()
        asset_type = self.__asset_type_extractor.extract(noun_phrase)
        
        # What about props ?
        return Declaration(txt, asset_type, 'assets', [])
