from app.classes.elements.standard_event_elements import ContractSubjectElement
from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.template_event.contract_components import ContractNouns

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 

# Not needed
class ContractSubjectUpdater(IUpdatePattern):
    def update(self, element: ContractSubjectElement, pattern: Pattern):
        if isinstance(pattern, EventPattern):
            pattern.event.subj = ContractNouns.contract()
