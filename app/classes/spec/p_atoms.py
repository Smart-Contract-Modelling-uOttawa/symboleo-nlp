from app.classes.spec.symboleo_spec import PAtom, Proposition
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.spec.other_function import OtherFunction
from app.classes.spec.helpers import VariableDotExpression


class PAtomRecursive(PAtom):
    def __init__(self, inner: Proposition):
        self.inner = inner
    
    def to_sym(self):
        return f'({self.inner.to_sym()})'


class NegatedPAtom(PAtom):
    def __init__(self, negated: PAtom):
        self.negated = negated
    
    def to_sym(self):
        return f'not {self.negated.to_sym()}'


class PAtomPredicate(PAtom):
    def __init__(self, predicate_function: PredicateFunction):
        self.predicate_function = predicate_function
    
    def to_sym(self):
        return self.predicate_function.to_sym()


class PAtomFunction(PAtom):
    def __init__(self, function: OtherFunction):
        self.predicate_function = function
    
    def to_sym(self):
        return super().to_sym()


# class PAtomEnum(PAtom):
#     def __init__(self, enumeration: Enumeration, enum_item: EnumItem):
#         self.enumeration = enumeration
#         self.enum_item = enum_item
    
#     def to_sym(self):
#         return f'{self.enumeration.to_sym()}({self.enum_item.to_sym()})'


class PAtomVariable(PAtom):
    def __init__(self, variable: VariableDotExpression):
        self.variable = variable
    
    def to_sym(self):
        return self.variable.to_sym()

