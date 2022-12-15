from app.classes.spec.sym_event import *
from app.classes.spec.sym_point import *
from app.classes.spec.sym_situation import * 
from app.classes.spec.helpers import *
from app.classes.spec.predicate_function import *

# Predicate: Key component to be updated in an obligation
Predicate = PredicateFunctionHappens or \
    PredicateFunctionHappensAfter or \
    PredicateFunctionHappensWithin or \
    PredicateFunctionWHappensBefore or \
    PredicateFunctionWHappensBeforeEvent or \
    PredicateFunctionOccurs
    #...?

# The main arguments for a predicate
Parameter = SymPoint or SymEvent or SymInterval or SymSituation


AllParameters = [
    SymPoint,
    SymEvent
]

# The components that make up parameters. 
# Will often be leaves in the graph structure, but not necessary
Primitive = VariableDotExpression or \
    PointVDE or \
    VariableEvent or \
    ObligationEvent or \
    ContractEvent or \
    PowerEvent or \
    TimeValueInt or \
    TimeUnitStr or \
    ObligationState or \
    PowerState or \
    ContractState


# Components
Component = Predicate or Parameter or Primitive