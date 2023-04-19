from app.classes.selection.selected_node import SelectedNode
from app.classes.frames.all_frames import *
from app.classes.other.frame_event import FrameEvent

class PrepNode(SelectedNode):
    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)
        if is_event_frame(new_frame):
            fe: FrameEvent = new_frame.frame_event 
            fe.pps.append(self.value)
        
        return new_frame


class AdverbNode(SelectedNode):
    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)
        if is_event_frame(new_frame):
            fe: FrameEvent = new_frame.frame_event 
            fe.adverb = self.value
        
        return new_frame
    

class PredicateNode(SelectedNode):
    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)
        if is_event_frame(new_frame):
            fe: FrameEvent = new_frame.frame_event 
            fe.predicate = self.value
        
        return new_frame
    

class DobjNode(SelectedNode):
    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)
        if is_event_frame(new_frame):
            fe: FrameEvent = new_frame.frame_event 
            fe.dobj = self.value
        
        return new_frame


class VerbNode(SelectedNode):
    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)
        if is_event_frame(new_frame):
            fe: FrameEvent = new_frame.frame_event 
            fe.verb = self.value
        
        return new_frame

class SubjectNode(SelectedNode):
    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)
        if is_event_frame(new_frame):
            fe: FrameEvent = new_frame.frame_event 
            fe.subj = self.value
        
        return new_frame