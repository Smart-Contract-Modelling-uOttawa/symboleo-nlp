from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType
from app.classes.spec.sym_event import SymEvent

from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionWHappensBefore

class IfNode(SelectedNode):
    node_type = NodeType.IF

    def to_obj(self, default_event: SymEvent):
        if self.child.node_type == NodeType.STATE:
            evt = self.child.to_obj(default_event)    
            return PredicateFunctionHappens(evt)

        raise NotImplementedError('Oops!')
        