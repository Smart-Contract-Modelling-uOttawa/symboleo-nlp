from __future__ import annotations
from typing import List
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.selection.selected_node import SelectedNode
from app.classes.selection.selected_node import Basket
from app.classes.selection.all_nodes import node_type_to_class

class ISelection:
    def get_nodes(self) -> List[SelectedNode]:
        raise NotImplementedError()
    # May end up just passing a Norm instead of basket
    def to_obj(self, basket: Basket):
        raise NotImplementedError()
    def add_node(self, grammar_node: AbstractNode, value = None):
        raise NotImplementedError()
    def add_selected_node(self, node: SelectedNode, ind: int):
        raise NotImplementedError()
    

class Selection(ISelection):
    def __init__(self):
        # Should make this private and expose a function
        self.__nodes: List[SelectedNode] = []

    def get_nodes(self) -> List[SelectedNode]:
        return self.__nodes

    def to_obj(self, basket: Basket):
        return self.__nodes[0].to_obj(basket)


    def add_node(self, grammar_node: AbstractNode, value = None):
        # Set up the new node
        new_class = node_type_to_class[grammar_node.node_type]
        ind = len(self.__nodes)
        node = new_class(grammar_node.id, ind, value)
        self.add_selected_node(node, ind)
        
    
    def add_selected_node(self, node: SelectedNode, ind: int):
        self.__nodes.append(node)
        # Set parent and child. This seems wrong...
        if ind > 0:
            node.parent = self.__nodes[ind-1]
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
