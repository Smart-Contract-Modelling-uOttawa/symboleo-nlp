from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType
from app.classes.spec.sym_event import SymEvent

from app.classes.spec.sym_event import ObligationEvent

class ObligationEventNode(SelectedNode):
    node_type = NodeType.OBLIGATION_EVENT

    def to_obj(self, default_event: SymEvent):
        event_name = self.child.child.to_obj(default_event)
        ob_var = self.child.to_obj(default_event)
        return ObligationEvent(event_name, ob_var)