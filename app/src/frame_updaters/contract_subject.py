from app.classes.selection.contract_subject_node import ContractSubjectNode
from app.classes.frames.frame import Frame, EventFrame

from app.src.frame_updaters.frame_updater import IUpdateFrame 

class ContractSubjectUpdater(IUpdateFrame):
    def update_frame(self, node: ContractSubjectNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.event.subj = node.value
