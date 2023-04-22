from app.classes.selection.custom_event_node import *
from app.classes.frames.frame import Frame, EventFrame

from app.src.frame_updaters.frame_updater import IUpdateFrame 


class PrepPhraseUpdater(IUpdateFrame):
    def update_frame(self, node: PrepNode, frame: Frame):
        if isinstance(frame, EventFrame):
            if not frame.event.pps:
                frame.event.pps = [node.value]
            else:
                frame.event.pps.append(node.value)


class AdverbUpdater(IUpdateFrame):
    def update_frame(self, node: AdverbNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.event.adverb = node.value

class PredicateUpdater(IUpdateFrame):
    def update_frame(self, node: PredicateNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.event.predicate = node.value
            

class DobjUpdater(IUpdateFrame):
    def update_frame(self, node: DobjNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.event.dobj = node.value


class VerbUpdater(IUpdateFrame):
    def update_frame(self, node: VerbNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.event.verb = node.value


class SubjectUpdater(IUpdateFrame):
    def update_frame(self, node: SubjectNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.event.subj = node.value

