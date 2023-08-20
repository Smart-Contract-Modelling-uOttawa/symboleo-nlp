from app.classes.spec.declaration import AssetDeclaration
from app.classes.events.custom_event.noun_phrase import NounPhrase, NPTextType
from app.classes.helpers.case_converter import CaseConverter

class IExtractAssetDeclarations:
    def extract(self, noun_phrase: NounPhrase) -> AssetDeclaration:
        raise NotImplementedError()


class AssetDeclarationExtractor(IExtractAssetDeclarations):
    def extract(self, noun_phrase: NounPhrase) -> AssetDeclaration:
        txt = noun_phrase.to_text(NPTextType.BASIC)
        asset_name = CaseConverter.to_snake(txt)
        asset_type = noun_phrase.asset_type
        return AssetDeclaration(asset_name, asset_type)
