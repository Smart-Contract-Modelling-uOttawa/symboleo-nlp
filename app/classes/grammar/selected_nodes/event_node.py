from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType
from app.classes.spec.sym_event import SymEvent

class EventNode(SelectedNode):
    node_type = NodeType.EVENT

    def to_obj(self, default_event: SymEvent):
        return self.child.to_obj(default_event)