from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.custom_event.noun_phrase import NounPhrase
from app.src.extractors.value_extractor import IExtractValue

from tests.helpers.test_objects import NounPhrases

# So that we don't need to use nlp
class FakeNounPhraseExtractor(IExtractValue[NounPhrase]):    
    def __init__(self):
        self.__dict = {
            'apple pie': NounPhrases.apple_pie(),
            'bob': NounPhrases.bob(),
            'buyer': NounPhrases.buyer(),
            'legal proceedings': NounPhrases.legal_proceedings(),
            'pets': NounPhrases.pets(),
            'credit card': NounPhrases.credit_card(),
            'the property': NounPhrases.property(),
            'the original digital photo files': NounPhrases.photos(),
            'Dolphin': NounPhrases.dolphin()
        }

    def extract(self, str_val: str, contract: SymboleoContract = None) -> NounPhrase:
        if str_val in self.__dict:
            return self.__dict[str_val]
        else:
            print(f'{str_val} not found in fake NP extractor dict...Please add')
            return NounPhrase(str_val, str_val)
        