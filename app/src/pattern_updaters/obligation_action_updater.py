from app.classes.selection.standard_event_node import ObligationActionNode
from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.custom_event.predicate import Predicate
from app.classes.template_event.contract_components import HelperVerbs

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 

class ObligationActionUpdater(IUpdatePattern):
    def update(self, node: ObligationActionNode, pattern: EventPattern):
        str_val = str(node.value.value).lower()
        pattern.event.predicate = Predicate(str_val)
        pattern.event.verb = HelperVerbs.verb_is()