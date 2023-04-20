from app.classes.selection.new_event_nodes import *
from app.classes.frames.frame import Frame, EventFrame

from app.src.frame_updaters.frame_updater import IUpdateFrame 


class PrepPhraseUpdater(IUpdateFrame):
    def update_frame(self, node: PrepNode, frame: Frame):
        if isinstance(frame, EventFrame):
            if not frame.frame_event.pps:
                frame.frame_event.pps = [node.value]
            else:
                frame.frame_event.pps.append(node.value)


class AdverbUpdater(IUpdateFrame):
    def update_frame(self, node: AdverbNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.frame_event.adverb = node.value

class PredicateUpdater(IUpdateFrame):
    def update_frame(self, node: PredicateNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.frame_event.predicate = node.value
            

class DobjUpdater(IUpdateFrame):
    def update_frame(self, node: DobjNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.frame_event.dobj = node.value


class VerbUpdater(IUpdateFrame):
    def update_frame(self, node: VerbNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.frame_event.verb = node.value


class SubjectUpdater(IUpdateFrame):
    def update_frame(self, node: SubjectNode, frame: Frame):
        if isinstance(frame, EventFrame):
            frame.frame_event.subj = node.value

