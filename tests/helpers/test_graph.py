import networkx as nx

from app.classes.graph.digraph import Digraph
from app.classes.graph.graph_node import GraphNode
class TestGraph:

    @staticmethod
    def get_digraph() -> Digraph:
        nodes: list[GraphNode] = []

        nodes.append(GraphNode('a', 'ROOT', ['b', 'c'], []))
        nodes.append(GraphNode('b', 'subclass', ['c', 'd'], []))
        nodes.append(GraphNode('c', 'subclass', [], ['e', 'f']))
        nodes.append(GraphNode('d', 'subclass', [], ['d']))
        nodes.append(GraphNode('d', 'prop', [], ['e', 'g']))
        nodes.append(GraphNode('e', 'prop', [], []))
        nodes.append(GraphNode('f', 'prop', [], []))
        nodes.append(GraphNode('g', 'prop', [], []))

        return Digraph(nodes)


    @staticmethod
    def get_nx_graph():
        
        G = nx.DiGraph()

        G.add_node('a')
        G.add_node('b')
        G.add_node('c')
        G.add_node('d')

        G.add_edge('a', 'b')
        G.add_edge('a', 'c')
        G.add_edge('b', 'c')
        G.add_edge('c', 'd')

        return G