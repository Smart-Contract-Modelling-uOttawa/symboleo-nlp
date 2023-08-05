from typing import List

from app.classes.grammar.grammar_node import GrammarNode
from app.classes.units.unit_type import UnitType
from app.classes.units.input_unit import InputUnit
from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.grammar_builder.grammar_builder import IBuildGrammar
from app.src.pattern_builder.pattern_class_getter import IGetAllPatternClasses
from app.web_lib.grammar_storage import GrammarStorage
from app.src.grammar_builder.child_getter import IGetChildren
from app.classes.spec.parameter_config import PatternClassType

from app.src.grammar_builder.tree_printer import TreePrinter

class GrammarHandler:
    def __init__(
        self, 
        pattern_class_getter: IGetAllPatternClasses,
        grammar_builder: IBuildGrammar,
        grammar_storage: GrammarStorage,
        child_getter: IGetChildren
    ):
        self.__pattern_class_getter = pattern_class_getter
        self.__grammar_builder = grammar_builder
        self.__grammar_storage = grammar_storage
        self.__child_getter = child_getter


    def create(self, pattern_types: List[PatternClassType] = None) -> GrammarNode:
        pattern_classes = self.__pattern_class_getter.get(pattern_types)
        grammar_node = self.__grammar_builder.build(pattern_classes)

        self.__grammar_storage.store('XXX', grammar_node)
        return grammar_node


    def get_children(self, contract: SymboleoContract) -> List[InputUnit]:
        grammar_node = self.__grammar_storage.load('XXX')
        children = self.__child_getter.get(grammar_node, contract)
        return children


    def select_child(self, prev_unit: str):
        grammar_node = self.__grammar_storage.load('XXX')
        selected_child = [x for x in grammar_node.children if x.name == prev_unit]

        if len(selected_child) != 1:
            raise ValueError('Invalid tree...')
    
        self.__grammar_storage.store('XXX', selected_child[0])


