from app.classes.spec.sym_event import *
from app.classes.spec.sym_point import *
from app.classes.spec.sym_situation import * 
from app.classes.spec.helpers import *

# TODO: Get rid of VDE completely - replace with more specific ones (e.g. PointVDE)
Primitive = VariableDotExpression or \
    PointVDE or \
    EventVDE or \
    ObligationEvent or \
    ContractEvent or \
    PowerEvent or \
    TimeValueInt or \
    TimeUnit or \
    ObligationState or \
    PowerState or \
    ContractState


class ScoredPrimitive:
    def __init__(self, primitive: Primitive, score: float):
        self.primitive = primitive
        self.score = score