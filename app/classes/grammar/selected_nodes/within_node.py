from app.classes.grammar.selected_node import SelectedNode, Basket
from app.classes.grammar.node_type import NodeType

from app.classes.spec.sym_point import PointFunction
from app.classes.spec.predicate_function import PredicateFunctionWHappensBefore

class WithinNode(SelectedNode):
    node_type = NodeType.WITHIN

    def to_obj(self, basket: Basket):
        time_info = self.child.to_obj(basket)
        event2 = self.child.child.to_obj(basket)
        p = PointFunction(event2, time_info[0], time_info[1])
        return PredicateFunctionWHappensBefore(basket.default_event, p)