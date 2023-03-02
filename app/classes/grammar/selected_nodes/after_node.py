from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType
from app.classes.spec.sym_event import SymEvent

from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent, PredicateFunctionHappensAfter

class AfterNode(SelectedNode):
    node_type = NodeType.AFTER

    def to_obj(self, default_event: SymEvent):       
        # Note: Uses the BeforeEvent, but swaps the order around... 
        if self.child.node_type == NodeType.EVENT:
            event2 = self.child.to_obj(default_event)
            return PredicateFunctionWHappensBeforeEvent(event2, default_event)

        elif self.child.node_type == NodeType.DATE:
            p = self.child.to_obj(default_event)
            return PredicateFunctionHappensAfter(default_event, p)

        raise NotImplementedError('Oops!')