from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType
from app.classes.spec.sym_event import SymEvent

from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent, PredicateFunctionWHappensBefore

class BeforeNode(SelectedNode):
    node_type = NodeType.BEFORE

    def to_obj(self, default_event: SymEvent):        
        if self.child.node_type == NodeType.EVENT:
            event2 = self.child.to_obj(default_event)
            return PredicateFunctionWHappensBeforeEvent(default_event, event2)

        elif self.child.node_type == NodeType.DATE:
            p = self.child.to_obj(default_event)
            return PredicateFunctionWHappensBefore(default_event, p)

        raise NotImplementedError('Oops!')