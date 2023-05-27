from app.classes.selection.standard_event_node import ContractSubjectNode
from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.template_event.contract_components import ContractNouns

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 

class ContractSubjectUpdater(IUpdatePattern):
    def update(self, node: ContractSubjectNode, pattern: Pattern):
        if isinstance(pattern, EventPattern):
            pattern.event.subj = ContractNouns.contract()
