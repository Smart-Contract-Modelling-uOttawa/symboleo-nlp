from app.classes.grammar.abstract_node import AbstractNode
from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.selected_nodes.all_nodes import node_type_to_class
from app.src.generator.selection import Selection

class ISelectGrammar:
    def select(self, root: AbstractNode) -> Selection:
        raise NotImplementedError()

class GrammarSelector(ISelectGrammar):
    def select(self, root_node: AbstractNode) -> Selection:
        # Init
        selection = Selection() 
        target = root_node
        list_head = self._convert_node(target)
        selection.add_node(list_head)

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
            next_node = self._convert_node(target, value)
            selection.add_node(next_node)
        
        return selection


    # Make this better?
    def _convert_node(self, node: AbstractNode, value = None) -> SelectedNode:
        new_class = node_type_to_class[node.node_type]
        return new_class(node.id, value)
    