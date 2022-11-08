import inspect
import copy
from app.classes.graph.digraph import Digraph
from app.src.string_to_class import StringToClass

class IConstructDynamicObjects:
    def construct(self, target_class: type, args):
        raise NotImplementedError()

class DynamicObjectConstructor(IConstructDynamicObjects):
    def __init__(self, graph: Digraph):
        self.__graph = graph
    
    # TODO: I need to copy the arg_set and then remove them so that they don't get re-used
    def construct(self, classname: type, arg_set):
        n_arg_set = [copy.deepcopy(x) for x in arg_set]
        target_class = StringToClass.convert(classname)
        signature = inspect.signature(target_class.__init__).parameters
        class_args = {}

        for k in signature:
            if k == 'self': 
                continue
            
            k_class = signature[k].annotation
            found_arg = [
                x for x in n_arg_set if self.__graph.is_subclass(type(x).__name__, k_class.__name__)
            ] 
            
            if len(found_arg) > 0:
                key = signature[k].name
                value = found_arg[0]
                n_arg_set.remove(value) # TODO: Maybe this works? Need to test...
                class_args[key] = value
            
        return target_class(**class_args)
