from app.classes.selection.contract_subject_node import ContractSubjectNode
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import BeforeDateFrame, AfterDateFrame

from app.src.frame_updaters.frame_updater import IUpdateFrame 

class DateUpdater(IUpdateFrame):
    def update_frame(self, node: ContractSubjectNode, frame: Frame):
        if isinstance(frame, (BeforeDateFrame, AfterDateFrame)):
            frame.date_text = node.value
