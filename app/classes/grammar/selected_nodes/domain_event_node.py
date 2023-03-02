from app.classes.grammar.selected_node import SelectedNode, Basket
from app.classes.grammar.node_type import NodeType
from app.classes.spec.sym_event import SymEvent

class DomainEventNode(SelectedNode):
    node_type = NodeType.DOMAIN_EVENT

    def to_obj(self, basket: Basket):
        return self.child.to_obj(basket)
