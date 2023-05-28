from app.classes.elements.custom_event_elements import *
from app.classes.patterns.pattern import EventPattern

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 


class PrepPhraseUpdater(IUpdatePattern):
    def update(self, element: PrepElement, pattern: EventPattern):
        if not pattern.event.pps:
            pattern.event.pps = [element.value]
        else:
            pattern.event.pps.append(element.value)

class AdverbUpdater(IUpdatePattern):
    def update(self, element: AdverbElement, pattern: EventPattern):
        pattern.event.adverb = element.value

class PredicateUpdater(IUpdatePattern):
    def update(self, element: PredicateElement, pattern: EventPattern):
        pattern.event.predicate = element.value
            

class DobjUpdater(IUpdatePattern):
    def update(self, element: DobjElement, pattern: EventPattern):
        pattern.event.dobj = element.value


class VerbUpdater(IUpdatePattern):
    def update(self, element: VerbElement, pattern: EventPattern):
        pattern.event.verb = element.value

class FailsToUpdater(IUpdatePattern):
    def update(self, element: FailsToElement, pattern: EventPattern):
        pattern.event.negation = True

class SubjectUpdater(IUpdatePattern):
    def update(self, element: SubjectElement, pattern: EventPattern):
        pattern.event.subj = element.value

