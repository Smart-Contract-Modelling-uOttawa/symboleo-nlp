from app.classes.custom_event.custom_event import CustomEvent
from app.classes.spec.domain_object import DomainEvent
from app.classes.template_event.EventMapping import EventMapping
from app.classes.template_event.common_events import CommonCustomEvents

from typing import Dict


# Next we need to know how we build the value_set
## I think this is a get_children thing
class DomainEventToCustomEvent:
    def map(self, domain_event: DomainEvent, value_set: Dict[str, EventMapping]) -> CustomEvent:
        custom_event = CommonCustomEvents.provide_termination_notice() # Can have a dict for this

        for x in domain_event.props:
            mp = value_set[x.key]
            if mp.evt_component == 'subject':
                custom_event.subj = mp.the_object

            if mp.evt_component == 'adverb':
                custom_event.adverb == mp.the_object
            
            ## Etc..
        
        return custom_event

