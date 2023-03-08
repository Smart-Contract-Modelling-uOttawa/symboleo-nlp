from enum import Enum

class PAtomicExpression:
    def to_sym(self):
        raise NotImplementedError()
    

# NOTE: This one was added in to avoid recursion on the PNegAtom
# All the other subclasses of PAtomicExpression, will now be subclasses of PAtom
class PAtom:
    def to_sym(self):
        raise NotImplementedError()
        

# Normally, the "atom" is another PAtomicExpression, but I am avoiding recursion
class PNegAtom(PAtomicExpression):
    def __init__(self, atom: PAtom, negation: bool = False):
        self.atom = atom
        self.negation = negation
    
    def to_sym(self):
        result = self.atom.to_sym()
        if self.negation:
            result = f'not {result}'
        return result

class PAtomStringLiteral(PAtomicExpression):
    def __init__(self, value: str):
        self.value = value
    
    def to_sym(self):
        return self.value


class PComparisonOp(Enum):
    GEq = '>='
    LEq = '<='
    GT = '>'
    LT = '<'

class PComparison:
    def __init__(self, curr: PAtomicExpression, right: PAtomicExpression = None, op: PComparisonOp = PComparisonOp.GEq):
        self.curr = curr
        self.right = right
        self.op = op # ">=" | "<=" | ">" | "<"
    
    def to_sym(self):
        if self.right:
            return f' {self.op.value} '.join([self.curr.to_sym(), self.right.to_sym()])
        else:
            return self.curr.to_sym()


class PEqualityOp(Enum):
    Equal = '=='
    NotEqual = '!='

class PEquality:
    def __init__(self, curr: PComparison, right: PComparison = None, op: PEqualityOp = PEqualityOp.Equal):
        self.curr = curr
        self.right = right
        self.op = op
    
    def to_sym(self):
        if self.right:
            return f' {self.op.value} '.join([self.curr.to_sym(), self.right.to_sym()])
        else:
            return self.curr.to_sym()


class PAnd:
    def __init__(self, p_eqs: list[PEquality]):
        self.p_eqs = p_eqs
    
    def to_sym(self):
        return ' and '.join([x.to_sym() for x in self.p_eqs])


class Proposition:
    def __init__(self, p_ands: list[PAnd]):
        self.p_ands = p_ands
    
    def to_sym(self):
        return ' OR '.join([x.to_sym() for x in self.p_ands])


