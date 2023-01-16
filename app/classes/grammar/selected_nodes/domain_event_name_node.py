from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType

from app.classes.spec.sym_event import VariableEvent

class DomainEventNameNode(SelectedNode):
    node_type = NodeType.DOMAIN_EVENT_NAME

    def to_user_text(self) -> str:
        return f'{self.value} is completed'

    def to_obj(self):
        return VariableEvent(self.value)