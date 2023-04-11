from app.classes.selection.selected_node import SelectedNode, Basket
from app.classes.tokens.node_type import NodeType
from app.classes.spec.domain_object import DomainProp

# TODO: Probably get rid of this one for now...
class UsingNode(SelectedNode):
    node_type = NodeType.USING

    def to_obj(self, basket: Basket):

        # Adds a norm -> Creates a power to suspend the initial norm 
        if self.child.node_type == NodeType.INSTRUMENT:
            instrument = self.child.to_obj(basket) # Just get the object text...
            # Likely would need to be declaration
            new_dm = DomainProp('instrument', 'str')
            return new_dm

        raise NotImplementedError('Oops!')