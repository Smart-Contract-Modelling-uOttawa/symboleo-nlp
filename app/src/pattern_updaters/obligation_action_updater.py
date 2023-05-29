from app.classes.elements.standard_event_elements import ObligationActionElement
from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.custom_event.base_event import StandardObligationEvent
from app.classes.custom_event.predicate import Predicate
from app.classes.template_event.contract_components import HelperVerbs

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 

class ObligationActionUpdater(IUpdatePattern):
    def update(self, element: ObligationActionElement, pattern: EventPattern):
        if isinstance(pattern.event, StandardObligationEvent):
            pattern.event.action = element.value.value
        else:
            pattern.event = StandardObligationEvent()
            pattern.event.action = element.value.value
        