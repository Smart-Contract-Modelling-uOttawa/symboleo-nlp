from typing import List
from app.classes.spec.domain_object import Role, Asset
from app.classes.other.noun_phrase import NounPhrase

class IExtractNounPhrase:
    def extract(self, str_val: str) -> NounPhrase:
        raise NotImplementedError()

# Need to decide if I'll inject contract info or if its an arg
## I think it should be an arg...

class NounPhraseExtractor:    
    def __init__(self, nlp):
        self.__nlp = nlp
        # Can I inject contract info in here.. to get the roles

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
        
    
        return NounPhrase(str_val, head.text, is_plural, is_role, is_asset, det, adjs)
