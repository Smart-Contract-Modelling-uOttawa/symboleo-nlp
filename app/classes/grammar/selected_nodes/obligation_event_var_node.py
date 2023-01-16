from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType

class ObligationEventVarNode(SelectedNode):
    node_type = NodeType.OBLIGATION_EVENT_VAR

    def to_user_text(self) -> str:
        return f'the {self.value} obligation'

    def to_obj(self):
        return self.value
