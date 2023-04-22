from app.classes.selection.selected_node import SelectedNode
from app.classes.frames.frame import Frame

class IUpdateFrame:
    def update_frame(self, node: SelectedNode, frame: Frame):
        raise NotImplementedError()

class DefaultFrameUpdater(IUpdateFrame):
    def update_frame(self, node: SelectedNode, frame: Frame):
        return frame
