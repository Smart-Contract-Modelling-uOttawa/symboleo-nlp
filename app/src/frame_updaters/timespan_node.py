from app.classes.selection.timepoint_node import TimepointNode
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import WithinTimespanEventFrame

from app.src.frame_updaters.frame_updater import IUpdateFrame 

class TimespanUpdater(IUpdateFrame):
    def update_frame(self, node: TimepointNode, frame: Frame):
        if isinstance(frame, WithinTimespanEventFrame):
            frame.timespan = node.value