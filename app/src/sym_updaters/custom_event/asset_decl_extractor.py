from app.classes.spec.declaration import AssetDeclaration
from app.classes.custom_event.noun_phrase import NounPhrase, NPTextType
from app.src.helpers.string_to_class import CaseConverter

# May want to pass in frame event for more context...
class IExtractAssetDeclarations:
    def extract(self, noun_phrase: NounPhrase) -> AssetDeclaration:
        raise NotImplementedError()


class AssetDeclarationExtractor(IExtractAssetDeclarations):
    def extract(self, noun_phrase: NounPhrase) -> AssetDeclaration:
        # default case
        txt = noun_phrase.to_text(NPTextType.BASIC)
        asset_name = CaseConverter.to_snake(txt)
        asset_type = noun_phrase.asset_type
        
        # What about props ?
        return AssetDeclaration(asset_name, asset_type)
