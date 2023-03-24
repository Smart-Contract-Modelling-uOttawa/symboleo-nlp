from app.classes.grammar.abstract_node import AbstractNode
from app.src.grammar.grammar_selector import ISelectGrammarNodes

class ManualGrammarNodeSelector(ISelectGrammarNodes):
    def select(self, target: AbstractNode) -> AbstractNode:
        print('\nChoose an option:')
        children_dict = {i+1: target.children[i] for i in range(0, len(target.children))}

        # User selects next child
        for ci in children_dict:
            cn = children_dict[ci]
            print('-', ci, cn.prompt)
        
        # Get the value. Sometimes auto, sometimes from user
        k = input("Enter target id: ")
        result = children_dict[int(k)]
        return result