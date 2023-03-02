from app.classes.grammar.selected_node import SelectedNode, Basket
from app.classes.grammar.node_type import NodeType

from app.classes.spec.sym_event import ObligationEvent

class ObligationEventNode(SelectedNode):
    node_type = NodeType.OBLIGATION_EVENT

    def to_obj(self, basket: Basket):
        event_name = self.child.child.to_obj(basket)
        ob_var = self.child.to_obj(basket)
        return ObligationEvent(event_name, ob_var)