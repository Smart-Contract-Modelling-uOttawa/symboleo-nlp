from app.classes.selection.custom_event_node import *
from app.classes.patterns.pattern import EventPattern

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 


class PrepPhraseUpdater(IUpdatePattern):
    def update(self, node: PrepNode, pattern: EventPattern):
        if not pattern.event.pps:
            pattern.event.pps = [node.value]
        else:
            pattern.event.pps.append(node.value)

class AdverbUpdater(IUpdatePattern):
    def update(self, node: AdverbNode, pattern: EventPattern):
        pattern.event.adverb = node.value

class PredicateUpdater(IUpdatePattern):
    def update(self, node: PredicateNode, pattern: EventPattern):
        pattern.event.predicate = node.value
            

class DobjUpdater(IUpdatePattern):
    def update(self, node: DobjNode, pattern: EventPattern):
        pattern.event.dobj = node.value


class VerbUpdater(IUpdatePattern):
    def update(self, node: VerbNode, pattern: EventPattern):
        pattern.event.verb = node.value

class FailsToUpdater(IUpdatePattern):
    def update(self, node: FailsToNode, pattern: EventPattern):
        pattern.event.negation = True

class SubjectUpdater(IUpdatePattern):
    def update(self, node: SubjectNode, pattern: EventPattern):
        pattern.event.subj = node.value

