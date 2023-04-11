from app.classes.selection.selected_node import SelectedNode, Basket
from app.classes.tokens.node_type import NodeType

class RootNode(SelectedNode):
    node_type = NodeType.ROOT

    def to_obj(self, basket: Basket):
        return self.child.to_obj(basket)