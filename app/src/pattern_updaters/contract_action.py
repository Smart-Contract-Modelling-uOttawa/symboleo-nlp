from app.classes.elements.standard_event_node import ContractActionNode
from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.template_event.contract_components import ContractVerbs

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 

class ContractActionUpdater(IUpdatePattern):
    def update(self, node: ContractActionNode, pattern: Pattern):
        if isinstance(pattern, EventPattern):
            pattern.event.verb = ContractVerbs.contract_verb_dict[node.value]()
            pattern.event.event_type = 'contract'
            # Could set the frame.event to be something different, e.g. ContractEvent
            ## double-name contractEvent - not great...