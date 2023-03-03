from app.classes.grammar.selected_node import SelectedNode, Basket
from app.classes.grammar.node_type import NodeType
from app.classes.spec.domain_model import DomainProp

class UsingNode(SelectedNode):
    node_type = NodeType.USING

    def to_obj(self, basket: Basket):

        # Adds a norm -> Creates a power to suspend the initial norm 
        if self.child.node_type == NodeType.INSTRUMENT:
            instrument = self.child.to_obj(basket) # Just get the object text...
            new_dm = DomainProp('instrument', instrument, 'str')
            return new_dm

        raise NotImplementedError('Oops!')