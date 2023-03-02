from app.classes.grammar.selected_node import SelectedNode, Basket
from app.classes.grammar.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import *

from app.classes.spec.helpers import TimeUnitStr, TimeValueInt

class TimespanNode(SelectedNode):
    node_type = NodeType.TIMESPAN

    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)

        if isinstance(new_frame, WithinTimespanEventFrame):
            new_frame.timespan = f'{self.value}'
        
        return new_frame


    def to_obj(self, basket: Basket):
        # Will need to split up the self.value... maybe just by a space?
        (tvi,tsu)  = self.value.split(' ')
        
        # Or maybe the value will be a dynamic type?
        time_value = TimeValueInt(tvi)
        time_unit = TimeUnitStr(tsu)

        return (time_value, time_unit) # Maybe a new object?