from app.classes.selection.selected_node import SelectedNode, Basket
from app.classes.tokens.node_type import NodeType

from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionWHappensBefore

class IfNode(SelectedNode):
    node_type = NodeType.IF

    def to_obj(self, basket: Basket):
        if self.child.node_type == NodeType.EVENT:
            evt = self.child.to_obj(basket)    
            return PredicateFunctionHappens(evt)

        raise NotImplementedError('Oops!')
        