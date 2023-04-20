from app.classes.spec.norm import INorm
from app.classes.selection.selected_node import SelectedNode
from app.classes.other.contract_update_obj import UpdatePackage
from app.classes.frames.frame import Frame

# An alternate way would be frame.update(node)
## But that would require a bunch of switch statemetns, etc..
class IUpdateFrame:
    def update_frame(self, node: SelectedNode, frame: Frame):
        raise NotImplementedError()

class DefaultFrameUpdater(IUpdateFrame):
    def update_frame(self, node: SelectedNode, frame: Frame):
        return frame
