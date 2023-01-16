from typing import List
from app.classes.grammar.selected_node import SelectedNode

class FrameChecker:
    @staticmethod
    def check(node_list: List[SelectedNode], pattern):
        if len(node_list) < len(pattern):
            return True
        
        node_list_types = [x.node_type for x in node_list]
        return FrameChecker.subfinder(node_list_types, pattern)

    @staticmethod
    def subfinder(test_list, sublist):
        res = False
        for idx in range(len(test_list) - len(sublist) + 1):
            if test_list[idx: idx + len(sublist)] == sublist:
                res = True
                break

        return res

