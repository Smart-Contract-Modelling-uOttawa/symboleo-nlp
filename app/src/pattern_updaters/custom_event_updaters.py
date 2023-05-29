from app.classes.elements.custom_event_elements import *
from app.classes.patterns.pattern import EventPattern

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 


class PrepPhraseUpdater(IUpdatePattern):
    def update(self, element: PrepElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            if not pattern.event.pps:
                pattern.event.pps = [element.value]
            else:
                pattern.event.pps.append(element.value)

class AdverbUpdater(IUpdatePattern):
    def update(self, element: AdverbElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            pattern.event.adverb = element.value

class PredicateUpdater(IUpdatePattern):
    def update(self, element: PredicateElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            pattern.event.predicate = element.value
            

class DobjUpdater(IUpdatePattern):
    def update(self, element: DobjElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            pattern.event.dobj = element.value


class VerbUpdater(IUpdatePattern):
    def update(self, element: VerbElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            pattern.event.verb = element.value

class FailsToUpdater(IUpdatePattern):
    def update(self, element: FailsToElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            pattern.event.negation = True

class SubjectUpdater(IUpdatePattern):
    def update(self, element: SubjectElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            pattern.event.subj = element.value

