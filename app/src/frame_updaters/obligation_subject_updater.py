from app.classes.selection.standard_event_node import ObligationSubjectNode
from app.classes.frames.frame import Frame, EventFrame
from app.classes.custom_event.noun_phrase import NounPhrase

from app.src.frame_updaters.frame_updater import IUpdateFrame 

class ObligationSubjectUpdater(IUpdateFrame):
    def update_frame(self, node: ObligationSubjectNode, frame: EventFrame):
        # May potentially make an ObligationNounPhrase that inherits from NounPhrase...
        subj = NounPhrase(
            str_val = node.value.to_text(),
            head = node.value.to_text()
        )
        frame.event.subj = subj
