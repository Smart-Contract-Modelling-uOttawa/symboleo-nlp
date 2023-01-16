from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType

from app.classes.spec.sym_event import ObligationEvent

class ObligationEventNode(SelectedNode):
    node_type = NodeType.OBLIGATION_EVENT

    def to_user_text(self) -> str:
        return None

    def to_obj(self):
        event_name = self.child.child.to_obj()
        ob_var = self.child.to_obj()
        return ObligationEvent(event_name, ob_var)