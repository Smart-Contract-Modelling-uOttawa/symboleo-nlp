import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import ContractEventName
from app.classes.patterns.pattern import EventPattern
from app.classes.elements.custom_event_elements import *

from app.src.pattern_updaters.contract_subject_updater import ContractSubjectUpdater

from app.classes.template_event.contract_components import ContractNouns

from app.src.pattern_updaters.custom_event_updaters import *

class CustomEventNodeUpdaterTests(unittest.TestCase):

    def test_prep_phrase_updater(self):
        prep_phrase = PrepPhrase('test', 'test', NounPhrase('a', 'b'))
        element = PrepElement(prep_phrase)
        pattern = EventPattern()

        sut = PrepPhraseUpdater()
        sut.update(element, pattern)
        self.assertEqual(pattern.event.pps[0], prep_phrase)
    

    def test_adverb_updater(self):
        adv = Adverb('test')
        element = AdverbElement(adv)
        pattern = EventPattern()

        sut = AdverbUpdater()
        sut.update(element, pattern)
        self.assertEqual(pattern.event.adverb, adv)
    

    def test_dobj_updater(self):
        np = NounPhrase('test', 'test')
        element = DobjElement(np)
        pattern = EventPattern()

        sut = DobjUpdater()
        sut.update(element, pattern)
        self.assertEqual(pattern.event.dobj, np)
    

    def test_predicate_updater(self):
        pred = Predicate('test')
        element = PredicateElement(pred)
        pattern = EventPattern()

        sut = PredicateUpdater()
        sut.update(element, pattern)
        self.assertEqual(pattern.event.predicate, pred)


    def test_verb_updater(self):
        verb = Verb('test', 'test', [], None)
        element = VerbElement(verb)
        pattern = EventPattern()

        sut = VerbUpdater()
        sut.update(element, pattern)
        self.assertEqual(pattern.event.verb, verb)
    

    def test_subj_updater(self):
        np = NounPhrase('test', 'test')
        element = SubjectElement(np)
        pattern = EventPattern()

        sut = SubjectUpdater()
        sut.update(element, pattern)
        self.assertEqual(pattern.event.subj, np)

if __name__ == '__main__':
    unittest.main()
