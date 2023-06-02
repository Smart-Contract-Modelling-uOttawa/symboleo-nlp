from app.classes.elements.standard_event_elements import ContractActionElement
from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.events.contract_events.standard_contract_event import StandardContractEvent

from app.src.pattern_builder.pattern_updaters.pattern_updater import IUpdatePattern 

class ContractActionUpdater(IUpdatePattern):
    def update(self, element: ContractActionElement, pattern: EventPattern):
        pattern.event = StandardContractEvent(element.value.value)
            