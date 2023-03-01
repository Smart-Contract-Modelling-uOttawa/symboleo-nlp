from typing import List
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.grammar.selected_node import SelectedNode
from app.classes.frames.frame import Frame
from app.classes.frames.frame_checker import FrameChecker

# This class handles the selection process
# It is fairly bulky and ill-defined - will need to trim it down as the program develops
class Selection:
    def __init__(self, possible_frames: List[Frame]):
        self.nodes: List[SelectedNode] = []
        self.possible_frames: List[Frame] = possible_frames

    def get_frames(self) -> List[Frame]:
        results: List[Frame] = []

        for frame in self.possible_frames:
            # Find all the nodes that have a match for the frame
            for node in self.nodes:
                frame = node.build_frame(frame)

            if frame.is_complete():
                results.append(frame)
                #text = frame.to_text()
                #results.append(text)
        
        return results

    def to_obj(self, default_event: PredicateFunction):
        # How do we handle the default event?
        ## Can pass it in as an optional parm to every to_obj func. May end up being important
        ## Can add it in after
        ## Probably best to add it as a parm - most things won't use it, but it may end up being useful...
        return self.nodes[0].to_obj(default_event)


    def add_node(self, node: SelectedNode):
        # Set index
        ind = len(self.nodes)
        node.ind = ind

        # Add it
        self.nodes.append(node)

        # Set parent and child. This seems wrong...
        if ind > 0:
            node.parent = self.nodes[ind-1]
            node.parent.child = node

        # check frames - only do this if there is more than one
        if len(self.possible_frames) > 1:
            new_frame_list = []
            for x in self.possible_frames:
                if FrameChecker.check(self.nodes, x.pattern):
                    new_frame_list.append(x)
            
            self.possible_frames = new_frame_list
        
        if len(self.possible_frames) == 0:
            raise NotImplementedError('No possible frames!')
        
        
    
        