from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType

from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent, PredicateFunctionWHappensBefore

class BeforeNode(SelectedNode):
    node_type = NodeType.BEFORE

    def to_obj(self):
        # need access to default event
        default_event = VariableEvent('test')
        
        if self.child.node_type == NodeType.EVENT:
            event2 = self.child.to_obj()
            return PredicateFunctionWHappensBeforeEvent(default_event, event2)

        elif self.child.node_type == NodeType.DATE:
            p = self.child.to_obj()
            return PredicateFunctionWHappensBefore(default_event, p)

        raise NotImplementedError('Oops!')