from app.classes.selection.date_node import DateNode
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import BeforeDateFrame, AfterDateFrame

from app.src.frame_updaters.frame_updater import IUpdateFrame 

class DateUpdater(IUpdateFrame):
    def update_frame(self, node: DateNode, frame: Frame):
        if isinstance(frame, (BeforeDateFrame, AfterDateFrame)):
            frame.date_text = node.value
