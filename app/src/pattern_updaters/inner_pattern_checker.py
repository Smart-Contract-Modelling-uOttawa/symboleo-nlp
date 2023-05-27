from typing import List
from app.classes.selection.selected_node import SelectedNode
from app.classes.units.node_type import NodeType

class IInnerPatternChecker:
    def check_pattern(self, node_list: List[SelectedNode], pattern_sequence: List[NodeType]) -> bool:
        raise NotImplementedError()

class InnerPatternChecker(IInnerPatternChecker):
    # This function does NOT care about patterns that MAY still be possible. 
    ## If needed, that will be separate
    def check_pattern(self, node_list: List[SelectedNode], pattern_sequence: List[NodeType]) -> bool:
        nt = [x.node_type for x in node_list]

        # If the pattern is longer than the node list, then we are not there yet
        if len(pattern_sequence) > len(nt):
            return False
        
        for i in range(len(pattern_sequence)):
            if pattern_sequence[i] != nt[i]:
                return False
        
        return True
    