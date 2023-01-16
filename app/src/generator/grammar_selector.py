from typing import List
from app.classes.grammar.abstract_node import AbstractNode
from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.selected_nodes.all_nodes import node_type_to_class

class ISelectGrammar:
    def select(self, root: AbstractNode) -> List[SelectedNode]:
        raise NotImplementedError()

class GrammarSelector(ISelectGrammar):
    def select(self, root_node: AbstractNode) -> List[SelectedNode]:
        # Init
        target = root_node
        list_head = self._convert_node(target)
        selected_nodes: List[SelectedNode] = [ list_head ]
        ind = 1

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
            parent = selected_nodes[ind-1] 
            next_node = self._convert_node(target, parent, value, ind)
            parent.add_child(next_node)
            selected_nodes.append(next_node)

            # Increment
            ind += 1

            curr_text = self._get_full_text(selected_nodes)
            print(f'\nCurrent text: {curr_text}\n')
        
        return selected_nodes
    
    def _get_full_text(self, selection: List[SelectedNode]) -> str:
        all_texts = [x.to_user_text() for x in selection]
        real_texts = [x for x in all_texts if x]
        result = ' '.join(real_texts)
        return result

    # Make this better?
    def _convert_node(self, node: AbstractNode, parent: AbstractNode = None, value = None, ind = 0) -> SelectedNode:
        new_class = node_type_to_class[node.node_type]
        result = new_class(node.id, parent, value, ind)
        return result
