import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import ContractEventName
from app.classes.frames.frame import EventFrame
from app.classes.selection.custom_event_node import *

from app.src.frame_updaters.contract_subject import ContractSubjectUpdater

from app.classes.template_event.contract_components import ContractNouns

from app.src.frame_updaters.custom_event_nodes import *

class CustomEventNodeUpdaterTests(unittest.TestCase):

    def test_prep_phrase_updater(self):
        prep_phrase = PrepPhrase('test', 'test', NounPhrase('a', 'b'))
        node = PrepNode(prep_phrase)
        frame = EventFrame()

        sut = PrepPhraseUpdater()
        sut.update_frame(node, frame)
        self.assertEqual(frame.event.pps[0], prep_phrase)
    

    def test_adverb_updater(self):
        adv = Adverb('test')
        node = AdverbNode(adv)
        frame = EventFrame()

        sut = AdverbUpdater()
        sut.update_frame(node, frame)
        self.assertEqual(frame.event.adverb, adv)
    

    def test_dobj_updater(self):
        np = NounPhrase('test', 'test')
        node = DobjNode(np)
        frame = EventFrame()

        sut = DobjUpdater()
        sut.update_frame(node, frame)
        self.assertEqual(frame.event.dobj, np)
    

    def test_predicate_updater(self):
        pred = Predicate('test')
        node = PredicateNode(pred)
        frame = EventFrame()

        sut = PredicateUpdater()
        sut.update_frame(node, frame)
        self.assertEqual(frame.event.predicate, pred)


    def test_verb_updater(self):
        verb = Verb('test', 'test', [], None)
        node = VerbNode(verb)
        frame = EventFrame()

        sut = VerbUpdater()
        sut.update_frame(node, frame)
        self.assertEqual(frame.event.verb, verb)
    

    def test_subj_updater(self):
        np = NounPhrase('test', 'test')
        node = SubjectNode(np)
        frame = EventFrame()

        sut = SubjectUpdater()
        sut.update_frame(node, frame)
        self.assertEqual(frame.event.subj, np)

if __name__ == '__main__':
    unittest.main()
