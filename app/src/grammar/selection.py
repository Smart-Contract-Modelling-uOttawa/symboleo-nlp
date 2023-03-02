from __future__ import annotations
from typing import List
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.grammar.abstract_node import AbstractNode
from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.selected_nodes.all_nodes import node_type_to_class

# This class handles the selection process
# It is fairly bulky and ill-defined - will need to trim it down as the program develops
class Selection:
    def __init__(self):
        self.nodes: List[SelectedNode] = []

    def to_obj(self, default_event: PredicateFunction):
        # How do we handle the default event?
        ## Can pass it in as an optional parm to every to_obj func. May end up being important
        ## Can add it in after
        ## Probably best to add it as a parm - most things won't use it, but it may end up being useful...
        return self.nodes[0].to_obj(default_event)

    def add_node(self, grammar_node: AbstractNode, value = None):
        # Set up the new node
        new_class = node_type_to_class[grammar_node.node_type]
        ind = len(self.nodes)
        node = new_class(grammar_node.id, ind, value)
        self.add_selected_node(node, ind)
        
    
    def add_selected_node(self, node: SelectedNode, ind: int):
        self.nodes.append(node)
        # Set parent and child. This seems wrong...
        if ind > 0:
            node.parent = self.nodes[ind-1]
            node.parent.child = node
    

    # For constructing the object from a set of selected nodes
    ## There is probably a way to make this cleaner
    @staticmethod
    def from_nodes(node_list: List[SelectedNode]) -> Selection:
        result = Selection()

        for i, node in enumerate(node_list):
            node.ind = i
            result.add_selected_node(node, i)
        
        return result
