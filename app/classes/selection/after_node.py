from app.classes.selection.selected_node import SelectedNode, Basket
from app.classes.tokens.node_type import NodeType
from app.classes.spec.sym_event import SymEvent

from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent, PredicateFunctionHappensAfter

class AfterNode(SelectedNode):
    node_type = NodeType.AFTER

    def to_obj(self, basket: Basket):       
        # Note: Uses the BeforeEvent, but swaps the order around... 
        if self.child.node_type == NodeType.EVENT:
            event2 = self.child.to_obj(basket)
            return PredicateFunctionWHappensBeforeEvent(event2, basket.default_event)

        elif self.child.node_type == NodeType.DATE:
            p = self.child.to_obj(basket)
            return PredicateFunctionHappensAfter(basket.default_event, p)

        raise NotImplementedError('Oops!')