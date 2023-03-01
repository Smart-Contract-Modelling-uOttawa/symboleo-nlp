from app.classes.spec.proposition import PAtom, Proposition
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.spec.other_function import OtherFunction
from app.classes.spec.helpers import VariableDotExpression

## Circular
# class PAtomRecursive(PAtom):
#     def __init__(self, inner: Proposition):
#         self.inner = inner
    
#     def to_sym(self):
#         return f'({self.inner.to_sym()})'


## TODO: Circular
## Likely just add a flag onto existing PAtom
# class NegatedPAtom(PAtom):
#     negated = PAtom() ## Circular...

#     def __init__(self, negated: PAtom):
#         self.negated = negated
    
#     def to_sym(self):
#         return f'not {self.negated.to_sym()}'


class PAtomPredicate(PAtom):
    predicate_function = PredicateFunction()

    def __init__(self, predicate_function: PredicateFunction):
        self.predicate_function = predicate_function
    
    def to_sym(self):
        return self.predicate_function.to_sym()


# class PAtomFunction(PAtom):
#     function: OtherFunction()

#     def __init__(self, function: OtherFunction):
#         self.function = function
    
#     def to_sym(self):
#         return super().to_sym()


# class PAtomEnum(PAtom):
#     def __init__(self, enumeration: Enumeration, enum_item: EnumItem):
#         self.enumeration = enumeration
#         self.enum_item = enum_item
    
#     def to_sym(self):
#         return f'{self.enumeration.to_sym()}({self.enum_item.to_sym()})'


# class PAtomVariable(PAtom):
#     def __init__(self, variable: VariableDotExpression):
#         self.variable = variable
    
#     def to_sym(self):
#         return self.variable.to_sym()

