from app.classes.selection.timespan_node import TimespanNode
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import WithinTimespanEventFrame
from app.classes.frames.all_frames import UntilTimespanFrame

from app.src.frame_updaters.frame_updater import IUpdateFrame 

class TimespanUpdater(IUpdateFrame):
    def update_frame(self, node: TimespanNode, frame: Frame):
        if isinstance(frame, (WithinTimespanEventFrame, UntilTimespanFrame)):
            frame.timespan = node.value
        