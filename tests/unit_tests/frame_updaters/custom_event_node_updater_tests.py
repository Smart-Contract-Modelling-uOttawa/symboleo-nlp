import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import ContractEventName
from app.classes.patterns.pattern import EventPattern
from app.classes.selection.custom_event_node import *

from app.src.pattern_updaters.contract_subject import ContractSubjectUpdater

from app.classes.template_event.contract_components import ContractNouns

from app.src.pattern_updaters.custom_event_nodes import *

class CustomEventNodeUpdaterTests(unittest.TestCase):

    def test_prep_phrase_updater(self):
        prep_phrase = PrepPhrase('test', 'test', NounPhrase('a', 'b'))
        node = PrepNode(prep_phrase)
        pattern = EventPattern()

        sut = PrepPhraseUpdater()
        sut.update(node, pattern)
        self.assertEqual(pattern.event.pps[0], prep_phrase)
    

    def test_adverb_updater(self):
        adv = Adverb('test')
        node = AdverbNode(adv)
        pattern = EventPattern()

        sut = AdverbUpdater()
        sut.update(node, pattern)
        self.assertEqual(pattern.event.adverb, adv)
    

    def test_dobj_updater(self):
        np = NounPhrase('test', 'test')
        node = DobjNode(np)
        pattern = EventPattern()

        sut = DobjUpdater()
        sut.update(node, pattern)
        self.assertEqual(pattern.event.dobj, np)
    

    def test_predicate_updater(self):
        pred = Predicate('test')
        node = PredicateNode(pred)
        pattern = EventPattern()

        sut = PredicateUpdater()
        sut.update(node, pattern)
        self.assertEqual(pattern.event.predicate, pred)


    def test_verb_updater(self):
        verb = Verb('test', 'test', [], None)
        node = VerbNode(verb)
        pattern = EventPattern()

        sut = VerbUpdater()
        sut.update(node, pattern)
        self.assertEqual(pattern.event.verb, verb)
    

    def test_subj_updater(self):
        np = NounPhrase('test', 'test')
        node = SubjectNode(np)
        pattern = EventPattern()

        sut = SubjectUpdater()
        sut.update(node, pattern)
        self.assertEqual(pattern.event.subj, np)

if __name__ == '__main__':
    unittest.main()
