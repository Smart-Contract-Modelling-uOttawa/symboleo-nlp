from app.classes.spec.sym_event import *
from app.classes.spec.sym_point import *
from app.classes.spec.sym_situation import * 

Primitive = VariableDotExpression or \
    ObligationEvent or \
    ContractEvent or \
    PowerEvent or \
    PointAtomObligationEvent or \
    PointAtomPowerEvent or \
    PointAtomContractEvent or \
    TimeValue or \
    ObligationState or \
    PowerState or \
    ContractState