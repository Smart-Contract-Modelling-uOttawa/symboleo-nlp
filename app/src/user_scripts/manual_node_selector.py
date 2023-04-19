from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.src.grammar.grammar_selector import ISelectGrammarNodes

class ManualGrammarNodeSelector(ISelectGrammarNodes):
    def select(self, node_set: List[AbstractNode]) -> AbstractNode:
        print('\nChoose an option:')
        node_dict = {i+1: node_set[i] for i in range(0, len(node_set))}

        # User selects next child
        for ci in node_dict:
            cn = node_dict[ci]
            print('-', ci, cn.prompt)

        print('\n')
        
        # Get the value. Sometimes auto, sometimes from user
        k = input("Enter target id: ")
        result = node_dict[int(k)]
        return result