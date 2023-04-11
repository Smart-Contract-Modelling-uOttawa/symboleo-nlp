from app.classes.selection.selected_node import SelectedNode, Basket
from app.classes.tokens.node_type import NodeType
from app.src.operations.build_norm import NormBuilder
from app.classes.spec.predicate_function import PredicateFunctionHappensWithin
from app.classes.spec.sym_event import ContractEvent
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.spec.sym_point import PointAtom, PointVDE, PointAtomContractEvent

class UntilNode(SelectedNode):
    node_type = NodeType.UNTIL

    def to_obj(self, basket: Basket):

        # Adds a norm -> Creates a power to suspend the initial norm 
        if self.child.node_type == NodeType.EVENT:
            evt = self.child.to_obj(basket)
            new_power = NormBuilder.build(basket.initial_norm, evt)
            return new_power

        # Refines to HappensWithin
        if self.child.node_type == NodeType.DATE:
            evt1 = ContractEvent('Activated')
            interval = Interval(IntervalFunction(
                PointAtomContractEvent(evt1),
                self.child.to_obj(basket)
            ))
            result = PredicateFunctionHappensWithin(basket.default_event, interval)
            return result

        raise NotImplementedError('Oops!')