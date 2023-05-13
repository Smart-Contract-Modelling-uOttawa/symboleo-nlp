from app.classes.selection.after_node import AfterNode
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import UntilTimespanFrame

from app.src.frame_updaters.frame_updater import IUpdateFrame 

class AfterUpdater(IUpdateFrame):
    def update_frame(self, node: AfterNode, frame: Frame):
        if isinstance(frame, UntilTimespanFrame):
            frame.prep = 'after'
