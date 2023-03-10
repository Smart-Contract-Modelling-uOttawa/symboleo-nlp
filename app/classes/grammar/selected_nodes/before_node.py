from app.classes.grammar.selected_node import SelectedNode, Basket
from app.classes.grammar.node_type import NodeType

from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent, PredicateFunctionWHappensBefore

class BeforeNode(SelectedNode):
    node_type = NodeType.BEFORE

    def to_obj(self, basket: Basket):        
        if self.child.node_type == NodeType.EVENT:
            event2 = self.child.to_obj(basket)
            return PredicateFunctionWHappensBeforeEvent(basket.default_event, event2)

        elif self.child.node_type == NodeType.DATE:
            p = self.child.to_obj(basket)
            return PredicateFunctionWHappensBefore(basket.default_event, p)

        elif self.child.node_type == NodeType.TIMEPOINT:
            p = self.child.to_obj(basket)
            return PredicateFunctionWHappensBefore(basket.default_event, p)

        raise NotImplementedError('Oops!')