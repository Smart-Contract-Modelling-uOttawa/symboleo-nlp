from app.classes.selection.selected_node import SelectedNode, Basket
from app.classes.tokens.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import *

class InstrumentNode(SelectedNode):
    node_type = NodeType.INSTRUMENT

    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)

        if isinstance(new_frame, UsingInstrumentFrame):
            # Can add NLP in here??
            new_frame.instrument = f'{self.value}'
        
        return new_frame


    def to_obj(self, basket: Basket):
        return self.value