from app.classes.elements.custom_event_elements import *
from app.classes.patterns.pattern import EventPattern

from app.src.pattern_builder.pattern_updaters.pattern_updater import IUpdatePattern 

# TODO: Can remove some of the event update functionality
## Since we've split off the nl_event and event (for sym) into separate pieces 
class PrepPhraseUpdater(IUpdatePattern):
    def update(self, element: PrepElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            if not pattern.event.pps:
                pattern.event.pps = [element.value]
            else:
                pattern.event.pps.append(element.value)

        if isinstance(pattern.nl_event, CustomEvent):
            if not pattern.nl_event.pps:
                pattern.nl_event.pps = [element.value]
            else:
                pattern.nl_event.pps.append(element.value)

class AdverbUpdater(IUpdatePattern):
    def update(self, element: AdverbElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            pattern.event.adverb = element.value
        
        if isinstance(pattern.nl_event, CustomEvent):
            pattern.nl_event.adverb = element.value

class PredicateUpdater(IUpdatePattern):
    def update(self, element: PredicateElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            pattern.event.predicate = element.value
        
        if isinstance(pattern.nl_event, CustomEvent):
            pattern.nl_event.predicate = element.value
            

class DobjUpdater(IUpdatePattern):
    def update(self, element: DobjElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            pattern.event.dobj = element.value
        
        if isinstance(pattern.nl_event, CustomEvent):
            pattern.nl_event.dobj = element.value


class VerbUpdater(IUpdatePattern):
    def update(self, element: VerbElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            pattern.event.verb = element.value
        
        if isinstance(pattern.nl_event, CustomEvent):
            pattern.nl_event.verb = element.value

class FailsToUpdater(IUpdatePattern):
    def update(self, element: FailsToElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            pattern.event.negation = True
        
        if isinstance(pattern.nl_event, CustomEvent):
            pattern.nl_event.negation = True

class SubjectUpdater(IUpdatePattern):
    def update(self, element: SubjectElement, pattern: EventPattern):
        if isinstance(pattern.event, CustomEvent):
            pattern.event.subj = element.value
        
        if isinstance(pattern.nl_event, CustomEvent):
            pattern.nl_event.subj = element.value

