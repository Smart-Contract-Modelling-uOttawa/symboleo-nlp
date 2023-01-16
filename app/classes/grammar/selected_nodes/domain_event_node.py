from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType

class DomainEventNode(SelectedNode):
    node_type = NodeType.DOMAIN_EVENT

    def to_user_text(self) -> str:
        return None

    def to_obj(self):
        return self.child.to_obj()
