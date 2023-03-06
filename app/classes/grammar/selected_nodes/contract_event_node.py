from app.classes.grammar.selected_node import SelectedNode, Basket
from app.classes.grammar.node_type import NodeType

from app.classes.spec.sym_event import ContractEvent, ContractEventName

class ContractEventNode(SelectedNode):
    node_type = NodeType.CONTRACT_EVENT

    def to_obj(self, basket: Basket):
        event_name = self.child.to_obj(basket)
        c_event_name = ContractEventName[str(event_name).capitalize()]
        return ContractEvent(c_event_name)