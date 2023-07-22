from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.src.custom_event_extractor.element_extractor import IExtractElement

from app.src.custom_event_extractor.noun_phrase.asset_type_extractor import IExtractAssetType

# TODO: Break this up: validation, determiner, head, adj, etc
## Maybe make a custom spacy-type of doc that can be passed around
class NounPhraseExtractor(IExtractElement[NounPhrase]):
    def __init__(
        self, 
        nlp,
        asset_type_extractor: IExtractAssetType
    ):
        self.__nlp = nlp
        self.__asset_type_extractor = asset_type_extractor

    def extract(self, str_val: str, contract: SymboleoContract = None) -> NounPhrase:
        doc = self.__nlp(str_val)

        # Validate
        ## Ensure that there is one noun_chunk

        # Get determiner
        if doc[0].tag_ == 'DT':
            det = doc[0].text
        else:
            det = None
        
        # Get the head
        heads = [x for x in doc if x.dep_ == 'ROOT']
        if len(heads) == 1:
            head = heads[0]
            is_plural = head.tag_ == 'NNS'
        else:
            raise ValueError('Invalid subject')
        
        # Get adjectives
        adjs = [x.text for x in doc 
            if x.tag_ == 'JJ' 
            or (x.dep_ == 'compound' and x.head.text == head.text)
        ]
        
        # Get Asset type
        asset_type = self.__asset_type_extractor.extract(str_val, head.text, contract)

        return NounPhrase(
            str_val, 
            head = head.text, 
            is_plural = is_plural, 
            is_role = (asset_type=='Role'),
            det = det, 
            adjs = adjs,
            asset_type = asset_type
        )
