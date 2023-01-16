from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType

from app.classes.spec.sym_point import PointVDE

class DateNode(SelectedNode):
    node_type = NodeType.DATE

    def to_user_text(self) -> str:
        return self.value

    def to_obj(self):
        return PointVDE(self.value)