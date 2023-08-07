from typing import List, Dict

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.grammar.grammar_node import GrammarNode
from app.classes.units.input_unit import InputUnit
from app.classes.operations.user_input import UserInput

from app.src.grammar_builder.child_getter import IGetChildren
from app.console_lib.input_converter import IConvertNodeToInput

class ISelectInput:
    def select(self, grammar_node: GrammarNode) -> List[InputUnit]:
        raise NotImplementedError()    

class InputSelector:
    def __init__(
        self, 
        input_converter: IConvertNodeToInput,
        child_getter: IGetChildren
    ):
        self.__input_converter = input_converter
        self.__child_getter = child_getter

    def select(self, grammar_node: GrammarNode, contract: SymboleoContract) -> List[UserInput]:
        results = []
        curr = grammar_node

        while True:
            children = self.__child_getter.get(curr, contract)

            if len(children) > 1:    
                input_unit = self._select_child(children)
            elif len(children) == 1:
                input_unit = self._default_select(children[0])
            else:
                break
            
            node_children = [x for x in curr.children if x.name == input_unit.unit_type.name]
            curr = node_children[0]

            next_result = self.__input_converter.convert(input_unit)
            results.append(next_result)
        
        return results
    

    def _select_child(self, children: List[InputUnit]) -> InputUnit:
        prompt = ''

        my_dict: Dict[int, GrammarNode] = {}
        for i, x in enumerate(children):
            k = i+1
            next_prompt = f'\n{k}: {x.prompt}'
            prompt += next_prompt
            my_dict[k] = x 

        print(prompt) 

        user_input = input('\nSelect a value: ')
        int_input = int(user_input)

        return my_dict[int_input]

            
    def _default_select(self, input_unit: InputUnit) -> InputUnit:
        prompt = f'\nDefault selection: {input_unit.prompt}'
        print(prompt)
        return input_unit
            