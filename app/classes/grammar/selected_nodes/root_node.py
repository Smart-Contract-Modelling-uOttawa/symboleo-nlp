from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType
from app.classes.spec.sym_event import SymEvent

class RootNode(SelectedNode):
    node_type = NodeType.ROOT

    def to_obj(self, default_event: SymEvent):
        return self.child.to_obj(default_event)