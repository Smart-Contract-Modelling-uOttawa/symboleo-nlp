from app.classes.selection.standard_event_node import ContractSubjectNode
from app.classes.frames.frame import Frame, EventFrame
from app.classes.template_event.contract_components import ContractNouns

from app.src.frame_updaters.frame_updater import IUpdateFrame 

class ContractSubjectUpdater(IUpdateFrame):
    def update_frame(self, node: ContractSubjectNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.event.subj = ContractNouns.contract()
