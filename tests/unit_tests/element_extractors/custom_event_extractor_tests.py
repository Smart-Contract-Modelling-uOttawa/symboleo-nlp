import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.custom_event import CustomEvent, Verb, NounPhrase
from app.classes.operations.user_input import UserInput, UnitType

from app.src.custom_event_extractor.element_extractor import IExtractElement
from app.src.custom_event_extractor.custom_event_extractor import CustomEventExtractor

from tests.helpers.test_objects import Verbs, NounPhrases

class CustomEventExtractorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fake_verb_extractor = IExtractElement[Verb]()
        fake_verb = Verbs.buys()
        self.fake_verb_extractor.extract = MagicMock(return_value=fake_verb)

        self.fake_np_extractor = IExtractElement[NounPhrase]()
        fake_subj = NounPhrases.bob()
        fake_dobj = NounPhrases.apple_pie()
        self.fake_np_extractor.extract = MagicMock(side_effect=[fake_subj, fake_dobj])

        # TODO: Fill this in...
        self.sut = CustomEventExtractor(
            self.fake_verb_extractor,
            self.fake_np_extractor,
            None,
            None,
            None
        )


    def test_custom_event_extractor(self):
        
        input_list = [
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'bob'),
            UserInput(UnitType.TRANSITIVE_VERB, 'buys'),
            UserInput(UnitType.DOBJ, 'apple pie')
        ]

        result = self.sut.extract(input_list, None)

        self.assertIsInstance(result, CustomEvent)
        self.assertEqual(self.fake_np_extractor.extract.call_count, 2)
        self.assertEqual(self.fake_verb_extractor.extract.call_count, 1)



if __name__ == '__main__':
    unittest.main()