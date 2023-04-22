from app.classes.selection.standard_event_node import ContractActionNode
from app.classes.frames.frame import Frame, EventFrame
from app.classes.template_event.contract_components import ContractVerbs

from app.src.frame_updaters.frame_updater import IUpdateFrame 

class ContractActionUpdater(IUpdateFrame):
    def update_frame(self, node: ContractActionNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.event.verb = ContractVerbs.contract_verb_dict[node.value]()