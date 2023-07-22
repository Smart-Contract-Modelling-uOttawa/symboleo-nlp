from typing import Dict, Type, List
from app.classes.units.input_unit import InputUnit, UnitType
from app.classes.spec.symboleo_contract import SymboleoContract

from app.classes.grammar.grammar_node import GrammarNode

from app.src.grammar_builder.unit_builders.unit_builder import IBuildUnit

class IGetChildren:
    def get(self, node: GrammarNode, contract: SymboleoContract) -> List[InputUnit]:
        raise NotImplementedError()

class ChildGetter(IGetChildren):
    def __init__(self, child_builder_dict: Dict[Type[InputUnit], IBuildUnit]):
        self.__dict = child_builder_dict
    
    def get(self, node: GrammarNode, contract: SymboleoContract) -> List[InputUnit]:
        results = []

        for x in node.children:
            unit_type = UnitType[x.name]
            op = self.__dict[unit_type]
            next_result = op.build(x.name, contract)
            results.append(next_result)

        return results
    