from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType

from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import PointFunction
from app.classes.spec.predicate_function import PredicateFunctionWHappensBefore

class WithinNode(SelectedNode):
    node_type = NodeType.WITHIN

    def to_user_text(self) -> str:
        return self.value

    def to_obj(self):
        default_event = VariableEvent('test')
        time_info = self.child.to_obj()
        event2 = self.child.child.to_obj()
        p = PointFunction(event2, time_info[0], time_info[1])
        return PredicateFunctionWHappensBefore(default_event, p)