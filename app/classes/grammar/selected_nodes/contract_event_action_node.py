from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType

class ContractEventActionNode(SelectedNode):
    node_type = NodeType.CONTRACT_EVENT_ACTION

    def to_user_text(self) -> str:
        return self.value

    def to_obj(self):
        return self.value