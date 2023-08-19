from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.src.custom_event_extractor.element_extractor import IExtractElement

from app.src.nlp.doc_parser import IParseDoc
from app.src.custom_event_extractor.noun_phrase.asset_type_extractor import IExtractAssetType

class NounPhraseExtractor(IExtractElement[NounPhrase]):
    def __init__(
        self, 
        doc_parser: IParseDoc,
        asset_type_extractor: IExtractAssetType
    ):
        self.__doc_parser = doc_parser
        self.__asset_type_extractor = asset_type_extractor

    def extract(self, str_val: str, contract: SymboleoContract = None) -> NounPhrase:
        doc = self.__doc_parser.parse(str_val)

        is_parm = False
        det = None
        adjs = []
        is_plural = False

        # Get determiner
        if doc.tokens[0].tag == 'DT':
            det = doc.tokens[0].text
        
        # Get the head
        heads = [x for x in doc.tokens if x.dep == 'ROOT']
        if len(heads) == 1:
            head = heads[0].text
            is_plural = heads[0].tag == 'NNS'
        else:
            raise ValueError('Invalid subject')
        
        # Get adjectives
        adjs = [x.text for x in doc.tokens
            if x.tag == 'JJ' 
            or (x.dep == 'compound' and x.head == head)
        ]
        
        # Get Asset type
        asset_type = self.__asset_type_extractor.extract(str_val, head, contract)

        return NounPhrase(
            str_val, 
            head = head, 
            is_plural = is_plural, 
            is_role = (asset_type.type_name=='Role'),
            det = det, 
            adjs = adjs,
            asset_type = asset_type.type_name,
            is_parm = is_parm,
            asset_id = asset_type.id
        )
