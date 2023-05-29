from app.classes.elements.standard_event_elements import ContractActionElement
from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.custom_event.base_event import StandardContractEvent
from app.classes.template_event.contract_components import ContractVerbs

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 

class ContractActionUpdater(IUpdatePattern):
    def update(self, element: ContractActionElement, pattern: EventPattern):
        pattern.event = StandardContractEvent(element.value.value)
            