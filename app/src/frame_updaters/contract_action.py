from app.classes.selection.contract_action_node import ContractActionNode
from app.classes.frames.frame import Frame, EventFrame

from app.src.frame_updaters.frame_updater import IUpdateFrame 


class ContractActionUpdater(IUpdateFrame):
    def update_frame(self, node: ContractActionNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.event.verb = node.value