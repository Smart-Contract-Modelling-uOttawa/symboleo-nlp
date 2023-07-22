import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.custom_event import CustomEvent, Verb, NounPhrase, Adverb, Predicate, PrepPhrase
from app.classes.events.custom_event.adverb import AdverbType
from app.classes.operations.user_input import UserInput, UnitType

from app.src.custom_event_extractor.element_extractor import IExtractElement
from app.src.custom_event_extractor.custom_event_extractor import CustomEventExtractor

from tests.helpers.test_objects import Verbs, NounPhrases

class CustomEventExtractorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fake_verb_extractor = IExtractElement[Verb]()
        fake_verb = Verbs.eats()
        self.fake_verb_extractor.extract = MagicMock(return_value=fake_verb)

        self.fake_np_extractor = IExtractElement[NounPhrase]()
        fake_subj = NounPhrases.bob()
        fake_dobj = NounPhrases.apple_pie()
        self.fake_np_extractor.extract = MagicMock(side_effect=[fake_subj, fake_dobj])

        self.fake_advb_extractor = IExtractElement[Adverb]()
        fake_advb = Adverb('noisily', [AdverbType.MANNER])
        self.fake_advb_extractor.extract = MagicMock(return_value = fake_advb)

        self.fake_pred_extractor = IExtractElement[Predicate]()
        fake_pred = Predicate('happy')
        self.fake_pred_extractor.extract = MagicMock(return_value=fake_pred)

        self.fake_pp_extractor = IExtractElement[PrepPhrase]()
        fake_pp = PrepPhrase('in canada', 'in', NounPhrases.canada())
        self.fake_pp_extractor.extract = MagicMock(return_value = fake_pp)
        
        self.sut = CustomEventExtractor(
            self.fake_verb_extractor,
            self.fake_np_extractor,
            self.fake_advb_extractor,
            self.fake_pred_extractor,
            self.fake_pp_extractor
        )



    def test_custom_event_extractor1(self):
        
        input_list = [
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'bob'),
            UserInput(UnitType.TRANSITIVE_VERB, 'eats'),
            UserInput(UnitType.DOBJ, 'apple pie'),
            UserInput(UnitType.ADVERB, 'noisily'),
            UserInput(UnitType.PREP_PHRASE, 'in canada')
        ]

        result = self.sut.extract(input_list, None)

        self.assertIsInstance(result, CustomEvent)
        self.assertEqual(self.fake_np_extractor.extract.call_count, 2)
        self.assertEqual(self.fake_verb_extractor.extract.call_count, 1)
        self.assertEqual(self.fake_advb_extractor.extract.call_count, 1)
        self.assertEqual(self.fake_pp_extractor.extract.call_count, 1)
    

    def test_custom_event_extractor2(self):    
        input_list = [
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'bob'),
            UserInput(UnitType.LINKING_VERB, 'is'),
            UserInput(UnitType.PREDICATE, 'happy')
        ]

        result = self.sut.extract(input_list, None)

        self.assertIsInstance(result, CustomEvent)
        self.assertEqual(self.fake_np_extractor.extract.call_count, 1)
        self.assertEqual(self.fake_verb_extractor.extract.call_count, 1)
        self.assertEqual(self.fake_pred_extractor.extract.call_count, 1)

    def test_custom_event_extractor_none(self):
        input_list = [
            UserInput(UnitType.EVENT)
        ]

        result = self.sut.extract(input_list, None)

        self.assertIsNone(result)



if __name__ == '__main__':
    unittest.main()