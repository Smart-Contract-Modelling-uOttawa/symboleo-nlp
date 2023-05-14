from __future__ import annotations
from app.classes.spec.proposition import PAtom
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.spec.other_predicates import OtherFunction

# In Symboleo, PAtomicExpression has many subclasses, which allow for recursive specification
# I am limiting recursion in this implementation
# The only subclass of PAtomicExpression now is PNegAtom, and this contains a PAtom member
# PAtom could therefore be the parent of the classes that are normally subclasses of PAtomicExpression

# Not included classes (Can be added as needed)
## PAtomEnum, tomVariable, PAtomDouble, PAtomStr, PAtomDate


class PAtomPredicate(PAtom):
    predicate_function = PredicateFunction()

    def __init__(self, predicate_function: PredicateFunction):
        self.predicate_function = predicate_function
    
    def __eq__(self, other: PAtomPredicate) -> bool:
        return self.predicate_function == other.predicate_function
    
    def to_sym(self):
        return self.predicate_function.to_sym()


class PAtomFunction(PAtom):
    function: OtherFunction()

    def __init__(self, function: OtherFunction):
        self.function = function
    
    def to_sym(self):
        return super().to_sym()


class PAtomPredicateTrueLiteral(PAtom):
    def __eq__(self, other: PAtomPredicateTrueLiteral) -> bool:
        return True
    
    def to_sym(self):
        return 'true'


class PAtomPredicateFalseLiteral(PAtom):
    def __eq__(self, other: PAtomPredicateFalseLiteral) -> bool:
        return True
    
    def to_sym(self):
        return 'F'



