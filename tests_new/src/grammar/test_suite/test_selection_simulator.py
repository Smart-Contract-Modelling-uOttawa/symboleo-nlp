from app.classes.grammar.abstract_node import AbstractNode
from app.classes.grammar.selected_node import SelectedNode
from app.src.generator.selection import Selection
from app.src.generator.grammar_selector import GrammarSelector

class SelectionSimulator:
    def simulate(self, root_node: AbstractNode, iv_list):
        i = 0
        curr_node = root_node
        selection = Selection()

        while i < len(iv_list):
            next_id, next_value = iv_list[i]
            next_node = [x for x in curr_node.children if x.id == next_id][0]

            selected_node = GrammarSelector._convert_node(next_node, next_value)
            selection.add_node(selected_node)
            curr_node = next_node
            i+=1
        
        return selection