from app.classes.elements.standard_event_elements import ContractSubjectElement
from app.classes.patterns.pattern import Pattern, EventPattern

from app.classes.events.template_event.contract_components import ContractNouns

from app.src.pattern_builder.pattern_updaters.pattern_updater import IUpdatePattern 

class ContractSubjectUpdater(IUpdatePattern):
    def update(self, element: ContractSubjectElement, pattern: EventPattern):
        pattern.nl_event.subj = ContractNouns.contract()
    
