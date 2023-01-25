from app.classes.grammar.abstract_node import AbstractNode
from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.selected_nodes.all_nodes import node_type_to_class
from app.src.generator.selection import Selection

class ISelectGrammar:
    def select(self, root: AbstractNode) -> Selection:
        raise NotImplementedError()

class GrammarSelector(ISelectGrammar):
    def __init__(self, selection: Selection):
        self.selection = selection

    def select(self, root_node: AbstractNode) -> Selection:
        # Init
        target = root_node
        list_head = self._convert_node(target)
        self.selection.add_node(list_head)

        while(len(target.children) > 0):
            print('\nChoose an option:')
            children_dict = {i+1: target.children[i] for i in range(0, len(target.children))}

            # User selects next child
            for ci in children_dict:
                cn = children_dict[ci]
                print('-', ci, cn.prompt)
            
            # Get the value. Sometimes auto, sometimes from user
            k = input("Enter target id: ")
            target = children_dict[int(k)]
            value = target.get_value()
            
            # Build the selected node
            next_node = GrammarSelector._convert_node(target, value)
            self.selection.add_node(next_node)
        
        return self.selection


    # Move this out...
    @staticmethod
    def _convert_node(node: AbstractNode, value = None) -> SelectedNode:
        new_class = node_type_to_class[node.node_type]
        return new_class(node.id, value)
    