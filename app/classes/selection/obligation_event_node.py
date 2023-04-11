from app.classes.selection.selected_node import SelectedNode, Basket
from app.classes.tokens.node_type import NodeType

from app.classes.spec.sym_event import ObligationEvent, ObligationEventName

class ObligationEventNode(SelectedNode):
    node_type = NodeType.OBLIGATION_EVENT

    def to_obj(self, basket: Basket):
        event_name = self.child.child.to_obj(basket)
        ob_var = self.child.to_obj(basket)
        ob_event_name = ObligationEventName[str(event_name).capitalize()]
        return ObligationEvent(ob_event_name, ob_var)