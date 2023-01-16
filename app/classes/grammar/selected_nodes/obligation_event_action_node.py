from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType

class ObligationEventActionNode(SelectedNode):
    node_type = NodeType.OBLIGATION_EVENT_ACTION

    # This is an example of where we need to access other parts of the structure
    # e.g. "is" or "being" depending on other parts
    def to_user_text(self) -> str:
        return f'is {self.value}'

    def to_obj(self):
        return self.value
