import unittest
from unittest.mock import MagicMock
from app.classes.spec.declaration import Declaration
from app.classes.spec.domain_object import DomainObject

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.custom_event import CustomEvent, Verb, NounPhrase, Adverb, Predicate, PrepPhrase
from app.classes.operations.user_input import UserInput, UnitType


from app.src.domain_updater.domain_update_extractor import DomainUpdateExtractor
from app.src.domain_updater.custom_event_extractor import IExtractCustomEvents
from app.src.domain_updater.asset_declaration_mapper import IMapAssetDeclarations
from app.src.domain_updater.event_declaration_mapper import IMapEventToDeclaration
from app.src.element_extractors.element_extractor import IExtractElement

from app.src.domain_updater.custom_event_extractor import CustomEventExtractor

from tests.helpers.test_objects import CustomEvents, Verbs, NounPhrases

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
            UserInput(UnitType.VERB, 'buys'),
            UserInput(UnitType.DOBJ, 'apple pie')
        ]

        result = self.sut.extract(input_list, None)

        self.assertIsInstance(result, CustomEvent)
        self.assertEqual(self.fake_np_extractor.extract.call_count, 2)
        self.assertEqual(self.fake_verb_extractor.extract.call_count, 1)



if __name__ == '__main__':
    unittest.main()