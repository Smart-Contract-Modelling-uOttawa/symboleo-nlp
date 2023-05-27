from typing import List, Dict, Type
from app.classes.selection.selected_node import SelectedNode
from app.classes.patterns.pattern import Pattern

from app.src.pattern_updaters.pattern_getter import IGetPattern
from app.src.pattern_updaters.pattern_updater import IUpdatePattern

class IBuildPatterns:
    def build(self, node_list: List[SelectedNode]) -> Pattern:
        raise NotImplementedError()

class PatternBuilder(IBuildPatterns):
    def __init__(
        self, 
        pattern_getter: IGetPattern,
        updater_dict: Dict[Type[SelectedNode], IUpdatePattern]
    ):
        self.__pattern_getter = pattern_getter
        self.__updater_dict = updater_dict


    def build(self, node_list: List[SelectedNode]) -> Pattern:
        pattern = self.__pattern_getter.get_pattern(node_list)

        for node in node_list:
            updater = self.__updater_dict[type(node)]
            updater.update(node, pattern)
        
        return pattern
