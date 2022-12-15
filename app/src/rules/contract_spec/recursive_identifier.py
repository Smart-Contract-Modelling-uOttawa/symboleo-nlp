from typing import Type, List
from app.src.rules.contract_spec.dynamic_constructor import IConstructDynamicObjects
from app.classes.graph.digraph import Digraph
from app.classes.processing.components import Parameter
from app.classes.processing.scored_components import ScoredPrimitive, ScoredParameter, ScoredParameterType, ScoredComponent
from app.src.string_to_class import StringToClass

class IIdentifyParametersRecursively:
    def identify(
        self, 
        target_class: Type[Parameter], 
        scored_components: List[ScoredComponent]
    ) -> ScoredParameter:
        raise NotImplementedError()

# Quite large: May want to break it up...
class RecursiveParameterIdentifier(IIdentifyParametersRecursively):
    def __init__(
        self, 
        graph: Digraph,
        dynamic_constructor: IConstructDynamicObjects
    ):
        self.__graph = graph
        self.__dynamic_constructor = dynamic_constructor
        self.__scored_components: List[ScoredComponent] = []
    

    def identify(
        self, 
        target_class: Type[Parameter], 
        scored_components: List[ScoredComponent]
    ) -> ScoredParameter:
        classname = target_class.__name__
        self.__scored_components = scored_components # May need to track these better?
        return self._rec_build(classname)


    def _rec_build(self, classname):
        graph_node = self.__graph.get_node(classname)
        #graph_node.print_me()

        # Base case
        match = self._handle_base(classname)
        if match:
            return match

        # Subclasses (OR)
        if len(graph_node.subclasses) > 0:
            rec_set = [self._rec_build(x) for x in graph_node.subclasses]
            if any(rec_set):
                return self._handle_or_set(rec_set, classname)
            else:
                return None
        
        # Props (AND)
        if len(graph_node.props) > 0:
            rec_set = [self._rec_build(x) for x in graph_node.props]
            if all(rec_set):
                return self._handle_and_set(rec_set, classname)
            else:
                return None

        return None


    def _handle_base(self, classname: str) -> ScoredComponent:
        matches = [x for x in self.__scored_components if type(x.obj).__name__ == classname]
        if matches:
            return max(matches, key=lambda x: x.score)
        return None


    def _handle_or_set(self, rec_set: List[ScoredPrimitive], classname: str):
        filtered_set = [x for x in rec_set if x is not None]
        # Find the one with the most arguments
        # Can also pick the highest score.
        return max(filtered_set, key = lambda x: len(x.obj.__dict__))


    def _handle_and_set(self, rec_set: List[ScoredPrimitive], classname: str):
        class_type = StringToClass.convert(classname)
        scored_type = ScoredParameterType(class_type, 1)
        result = self.__dynamic_constructor.construct(scored_type, rec_set)
        return ScoredPrimitive(result.obj, result.score)
