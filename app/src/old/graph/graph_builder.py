import inspect
from app.classes.graph.digraph import Digraph

# Note: Any class that is needed on the graph needs to be imported here
from app.classes.spec.p_atoms import * 
from app.classes.spec.point_function import *
from app.classes.graph.graph_node import GraphNode

class IBuildGraphs: # pragma: no cover
    def build(self, root: type) -> Digraph:
        raise NotImplementedError()

class GraphBuilder(IBuildGraphs):
    def __init__(self, max_depth = 5):
        self.max_depth = max_depth
        self.main_list = {}
        self.block_list = [
            'str',
            'DeferredConfigString',
            'LSString',
            'property',
        ]
    
    def build(self, root) -> Digraph:
        self.main_list = {}
        nodes = self._traverse(root, 'ROOT', d=0)
        return Digraph(nodes)

    def _traverse(self, C: type, unit_type: str, d = 0) -> list[GraphNode]:
        name = C.__name__

        if name in self.main_list:
            return []
        else:    
            self.main_list[name] = True

        subclass_names = C.__subclasses__()
        subclasses = [s for s in subclass_names if s.__name__ not in self.block_list]
        subclass_list = [s.__name__ for s in subclasses]

        mems = inspect.getmembers(C, lambda a:not(inspect.isroutine(a)))
        f_mems = [m for m in mems if m[0][0] != '_']
        props = [m for m in f_mems if m not in self.block_list]
        props_list = [type(m[1]).__name__ for m in props]

        result = []
        curr_node = GraphNode(name, unit_type, subclass_list, props_list)
        result.append(curr_node)
        
        for x in subclasses:
            next_subclass = self._traverse(x, 'subclass', d+1)
            result.extend(next_subclass)

        for y in props:
            next_prop = self._traverse(type(y[1]), 'prop', d+1)
            result.extend(next_prop)
            
        return result
