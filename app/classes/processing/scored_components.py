from typing import Type
from app.classes.processing.components import Component, Predicate, Parameter, Primitive

class ScoredComponent:
    def __init__(self, obj: Component, score: float):
        self.obj = obj 
        self.score = score

class ScoredPredicate(ScoredComponent):
    def __init__(self, predicate: Predicate, score: float):
        super().__init__(predicate, score)

class ScoredParameter(ScoredComponent):
    def __init__(self, parameter: Parameter, score: float):
        super().__init__(parameter, score)

class ScoredPrimitive(ScoredComponent):
    def __init__(self, primitive: Primitive, score: float):
        super().__init__(primitive, score)


class ScoredType:
    def __init__(self, obj_type: Type[Component], score: float):
        self.obj_type = obj_type 
        self.score = score

class ScoredPredicateType(ScoredType):
    def __init__(self, pred_type: Type[Predicate], score: float):
        super().__init__(pred_type, score)

class ScoredParameterType(ScoredType):
    def __init__(self, parm_type: Type[Parameter], score: float):
        super().__init__(parm_type, score)

    
