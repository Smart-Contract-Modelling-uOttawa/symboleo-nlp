from app.classes.other.noun_phrase import NounPhrase

import re

# May want to pass in frame event for more context...
# Also, do we include existing asset types on here as well?
# Might strongly type the return type as well
class IExtractAssetType:
    def extract(self, noun_phrase: NounPhrase) -> str:
        raise NotImplementedError()

# Challenge!
# This is where something like wordnet may be useful as well...
class AssetTypeExtractor(IExtractAssetType):
    def extract(self, noun_phrase: NounPhrase) -> str:
        money = re.search('\$\d+(?:\.\d+)?', noun_phrase.to_text())
        if money:
            return 'Amount'
        
        return 'String'
