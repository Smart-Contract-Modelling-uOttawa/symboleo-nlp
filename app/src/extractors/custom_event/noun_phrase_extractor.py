from typing import List
from app.classes.spec.domain_object import Role, Asset
from app.classes.custom_event.noun_phrase import NounPhrase

class IExtractNounPhrase:
    def extract(self, str_val: str) -> NounPhrase:
        raise NotImplementedError()

# TODO: More work on this
## Likely add contract in as arg for getting role/asset info
## May re-add the is_asset info (or even more detail... e.g. link to the asset)
# Also pull any NLP needs into separate interface
class NounPhraseExtractor(IExtractNounPhrase):
    def __init__(self, nlp):
        self.__nlp = nlp

    def extract(self, str_val: str) -> NounPhrase:
        doc = self.__nlp(str_val)
    
        is_role = False
        is_asset = False

        # Validate
        ## Ensure that there is one noun_chunk and it is equal

        # Get determiner
        if doc[0].tag_ == 'DT':
            det = doc[0].text
        else:
            det = None
        
        # Get adjectives
        adjs = [x.text for x in doc if x.tag_ == 'JJ']
        
        # Get the head
        heads = [x for x in doc if x.dep_ == 'ROOT']
        if len(heads) == 1:
            head = heads[0]
            is_plural = head.tag_ == 'NNS'
        else:
            raise ValueError('Invalid subject')
        
        # To figure out...
        # if self.__roles:
        #     role_list = [x.name for x in self.__roles]
        #     is_role = head in role_list or str_val in role_list
        
        # if self.__assets:
        #     asset_list = [x.name for x in self.__assets]
        #     is_asset = head in asset_list or str_val in asset_list
        
        return NounPhrase(
            str_val, 
            head = head.text, 
            is_plural = is_plural, 
            is_role = is_role,
            det = det, 
            adjs = adjs
        )
