from app.classes.selection.standard_event_node import ObligationActionNode
from app.classes.frames.frame import Frame, EventFrame
from app.classes.custom_event.predicate import Predicate
from app.classes.template_event.contract_components import HelperVerbs

from app.src.frame_updaters.frame_updater import IUpdateFrame 

class ObligationActionUpdater(IUpdateFrame):
    def update_frame(self, node: ObligationActionNode, frame: EventFrame):
        str_val = str(node.value.value).lower()
        frame.event.predicate = Predicate(str_val)
        frame.event.verb = HelperVerbs.verb_is()