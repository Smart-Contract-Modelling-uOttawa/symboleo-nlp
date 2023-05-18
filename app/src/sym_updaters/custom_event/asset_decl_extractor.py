from app.classes.spec.declaration import Declaration
from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.custom_event.noun_phrase import NounPhrase

# May want to pass in frame event for more context...
class IExtractAssetDeclarations:
    def extract(self, noun_phrase: NounPhrase) -> Declaration:
        raise NotImplementedError()


class AssetDeclarationExtractor(IExtractAssetDeclarations):
    def extract(self, noun_phrase: NounPhrase) -> Declaration:
        # default case
        txt = noun_phrase.to_text()
        asset_type = noun_phrase.asset_type
        
        # What about props ?
        return Declaration(txt, asset_type, 'assets', [])
