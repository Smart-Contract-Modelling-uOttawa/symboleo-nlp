from app.classes.grammar.selected_node import SelectedNode, Basket
from app.classes.grammar.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import *

from app.classes.spec.point_function import TimeUnit

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
        time_value = tvi
        time_unit = TimeUnit[tsu.capitalize()]

        return (time_value, time_unit) # Maybe a new object?