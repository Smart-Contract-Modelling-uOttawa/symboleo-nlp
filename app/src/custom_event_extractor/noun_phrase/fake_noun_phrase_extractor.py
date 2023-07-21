from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.src.custom_event_extractor.element_extractor import IExtractElement

from tests.helpers.test_objects import NounPhrases

# So that we don't need to use nlp
class FakeNounPhraseExtractor(IExtractElement[NounPhrase]): # pragma: no cover
    def __init__(self):
        self.__dict = {
            'apple pie': NounPhrases.apple_pie(),
            'bob': NounPhrases.bob(),

            'buyer': NounPhrases.buyer(),
            'seller': NounPhrases.the_seller(),

            'renter': NounPhrases.renter(),
            'landlord': NounPhrases.landlord(),
            'property': NounPhrases.property(),
            'the property': NounPhrases.property(),
            'property': NounPhrases.property(),

            'legal proceedings': NounPhrases.legal_proceedings(),
            'pets': NounPhrases.pets(),
            'credit card': NounPhrases.credit_card(),
            
            'the original digital photo files': NounPhrases.photos(),
            'Dolphin': NounPhrases.dolphin(),
            '$100': NounPhrases.hundred_dollars(),
            'CAD': NounPhrases.cad(),
            'March 30, 2024': NounPhrases.date_np('March 30, 2024'),

            'client': NounPhrases.client(),
            'contractor': NounPhrases.contractor(),
            'services': NounPhrases.services(),
            'disclosure': NounPhrases.disclosure(),

            'BOSCH': NounPhrases.bosch(),
            'CLIENT': NounPhrases.client_cap(),
            'productivity': NounPhrases.productivity(),

            'authorization': NounPhrases.authorization(),

        }

    def extract(self, str_val: str, contract: SymboleoContract = None) -> NounPhrase:
        if str_val in self.__dict:
            return self.__dict[str_val]
        else:
            print(f'{str_val} not found in fake NP extractor dict...Please add')
            return NounPhrase(str_val, str_val)
        