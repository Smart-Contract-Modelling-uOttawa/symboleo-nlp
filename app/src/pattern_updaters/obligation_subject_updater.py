from app.classes.elements.standard_event_elements import ObligationSubjectElement
from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.custom_event.base_event import StandardObligationEvent

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 

class ObligationSubjectUpdater(IUpdatePattern):
    def update(self, element: ObligationSubjectElement, pattern: EventPattern):
        if isinstance(pattern.event, StandardObligationEvent):
            pattern.event.ob_var = element.value
        else:
            pattern.event = StandardObligationEvent()
            pattern.event.ob_var = element.value.str_val

