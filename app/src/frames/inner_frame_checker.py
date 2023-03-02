from typing import List
from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType

class IInnerFrameChecker:
    def check_frame(self, node_list: List[SelectedNode]):
        raise NotImplementedError()

class InnerFrameChecker(IInnerFrameChecker):
    def check_frame(self, node_list: List[SelectedNode], pattern: List[NodeType]) -> bool:
        # If node list too short, then return True; still possible?
        # There's probably a better way to do this
        if len(node_list) < len(pattern):
            return True
        
        node_list_types = [x.node_type for x in node_list]
        return InnerFrameChecker._subfinder(node_list_types, pattern)


    @staticmethod
    def _subfinder(test_list, sublist) -> bool:
        for idx in range(len(test_list) - len(sublist) + 1):
            if test_list[idx: idx + len(sublist)] == sublist:
                return True

        return False