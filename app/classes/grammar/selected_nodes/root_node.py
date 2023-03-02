from app.classes.grammar.selected_node import SelectedNode, Basket
from app.classes.grammar.node_type import NodeType

class RootNode(SelectedNode):
    node_type = NodeType.ROOT

    def to_obj(self, basket: Basket):
        return self.child.to_obj(basket)