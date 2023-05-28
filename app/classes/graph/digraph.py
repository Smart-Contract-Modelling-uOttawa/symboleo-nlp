from app.classes.graph.graph_node import GraphNode

import networkx as nx

class Digraph:
    def __init__(self, nodes: list[GraphNode]):
        self.nodes = nodes
        self.__node_dict = {x.name: x for x in nodes}
        
    def leaves(self):
        return [x for x in self.nodes if len(x.subclasses) == 0 and len(x.props) == 0]
    
    def is_leaf(self, name):
        node = self.get_node(name)
        return len(node.subclasses) == 0 and len(node.props) == 0
    
    def get_node(self, name):
        return self.__node_dict[name]

    def is_subclass(self, a:str, b:str):
        if a == b: 
            return True
        
        node_b: GraphNode = self.get_node(b)
        if a in node_b.subclasses:
            return True
        
        for sc in node_b.subclasses:
            if self.is_subclass(a, sc):
                return True
        
        # New addition...
        for p in node_b.props:
            if self.is_subclass(a, p):
                return True
        
        return False

    def get_nx_graph(self):
        G = nx.DiGraph()
    
        for x in self.nodes:
            G.add_nodes_from([(x.name, {"unit_type": x.unit_type})])
        
        for x in self.nodes:
            for y in x.subclasses:
                G.add_edge(x.name, y)
            
            for y in x.props:
                G.add_edge(x.name, y)
        
        return G
    
