from app.classes.selection.contract_subject_node import ContractSubjectNode
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import BeforeTimePointFrame

from app.src.frame_updaters.frame_updater import IUpdateFrame 

class DomainTimepointUpdater(IUpdateFrame):
    def update_frame(self, node: ContractSubjectNode, frame: Frame):
        if isinstance(frame, (BeforeTimePointFrame)):
            frame.timepoint = node.value