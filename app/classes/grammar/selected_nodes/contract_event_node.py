from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType

from app.classes.spec.sym_event import ContractEvent

class ContractEventNode(SelectedNode):
    node_type = NodeType.CONTRACT_EVENT

    def to_obj(self):
        event_name = self.child.to_obj()
        return ContractEvent(event_name)