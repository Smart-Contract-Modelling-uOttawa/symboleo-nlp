from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType

from app.classes.spec.helpers import TimeUnitStr, TimeValueInt

class TimespanNode(SelectedNode):
    node_type = NodeType.TIMESPAN

    def to_user_text(self) -> str:
        return f'{self.value} of'

    def to_obj(self):
        # Will need to split up the self.value... maybe just by a space?
        # Or maybe the value will be a dynamic type?
        time_value = TimeValueInt(2)
        time_unit = TimeUnitStr('weeks')

        return (time_value, time_unit) # Maybe a new object?