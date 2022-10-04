from app.classes.graph.digraph import Digraph
from app.classes.spec.primitive import Primitive
from app.classes.spec.symboleo_spec import PNegAtom
from app.src.dynamic_constructor import IConstructDynamicObjects
from app.src.primitive_checker import ICheckPrimitives

class IBuildPredicates:
    def build(self, predicate: str, primitives: list[Primitive]) -> PNegAtom:
        raise NotImplementedError()
    
class PredicateBuilder(IBuildPredicates):
    def __init__(
        self, 
        graph: Digraph,
        primitive_checker: ICheckPrimitives,
        dynamic_constructor: IConstructDynamicObjects 
    ):
        self.__graph = graph
        self.__primitive_checker = primitive_checker
        self.__dynamic_constructor = dynamic_constructor

    def build(self, classname: str, primitives: list[Primitive]) -> PNegAtom:
        self.__primitives = primitives
        return self._rec_build(classname)
    
    def _rec_build(self, classname: str):
        # Get the node
        graph_node = self.__graph.get_node(classname)
    
        # base case: If it's a leaf node, then return it. Otherwise 'None'
        if self.__graph.is_leaf(classname):
            return self.__primitive_checker.check(classname, self.__primitives)

        # Subclasses (OR)
        if len(graph_node.subclasses) > 0:
            # Return the first item that is found (short-circuit)
            for sc in graph_node.subclasses:
                next_res = self._rec_build(sc)
                if next_res:
                    return next_res
            return None
        
        # Props (AND)
        if len(graph_node.props) > 0:
            rec_set = [self._rec_build(x) for x in graph_node.props]
            if all(rec_set):
                result = self.__dynamic_constructor.construct(classname, rec_set)
                return result
            else:
                return None