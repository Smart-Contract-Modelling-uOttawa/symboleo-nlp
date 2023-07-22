from typing import List, Dict
from app.classes.grammar.grammar_node import GrammarNode
from app.classes.units.input_unit import InputUnit
from app.classes.operations.user_input import UserInput

from app.console_lib.input_converter import IConvertNodeToInput

class ISelectInput:
    def select(self, grammar_node: GrammarNode) -> List[InputUnit]:
        raise NotImplementedError()    

class InputSelector:
    def __init__(self, input_converter: IConvertNodeToInput):
        self.__input_converter = input_converter

    def select(self, grammar_node: GrammarNode) -> List[UserInput]:
        results = []
        curr = grammar_node

        while True:
            if len(curr.children) > 1:
                selection = self._select_child(curr.children)
            elif len(curr.children) == 1:
                selection = self._default_select(curr.children[0])
            else:
                break

            next_result = self.__input_converter.convert(selection)
            results.append(next_result)
            
            # Convert 
            curr = selection
        
        return results
    

    def _select_child(self, children: List[GrammarNode]) -> GrammarNode:
        prompt = ''

        my_dict: Dict[int, GrammarNode] = {}
        for i, x in enumerate(children):
            k = i+1
            next_prompt = f'\n{k}: {x.name}'
            prompt += next_prompt
            my_dict[k] = x 

        print(prompt) 

        user_input = input('\nSelect a value: ')
        int_input = int(user_input)

        return my_dict[int_input]

            
    def _default_select(self, node: GrammarNode) -> GrammarNode:
        prompt = f'\nDefault selection: {node.name}'
        print(prompt)
        return node
            