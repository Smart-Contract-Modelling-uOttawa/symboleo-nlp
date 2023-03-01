class PAtom:
    def to_sym(self):
        raise NotImplementedError()
        
class PNegAtom:
    def __init__(self, atom: PAtom, negation: bool = False):
        self.atom = atom
        self.negation = negation
    
    def to_sym(self):
        result = self.atom.to_sym()
        if self.negation:
            result = f'not {result}'
        return result

class PComparison:
    def __init__(self, p_atoms: list[PNegAtom], op: str = ''):
        self.p_atoms = p_atoms
        self.op = op # ">=" | "<=" | ">" | "<"
    
    def to_sym(self):
        return f' {self.op} '.join([x.to_sym() for x in self.p_atoms])


class PEquality:
    def __init__(self, p_comps: list[PComparison], op: str = ''):
        self.p_comps = p_comps
        self.op = op # == or !=
    
    def to_sym(self):
        return f' {self.op} '.join([x.to_sym() for x in self.p_comps])

# TODO: May not need this... already have an 'AND' joiner... May need an OR joiner...
class PAnd:
    def __init__(self, p_eqs: list[PEquality]):
        self.p_eqs = p_eqs
    
    def to_sym(self):
        return ' AND '.join([x.to_sym() for x in self.p_eqs])

class Proposition:
    def __init__(self, p_ands: list[PAnd]):
        self.p_ands = p_ands
    
    def to_sym(self):
        return ' AND '.join([x.to_sym() for x in self.p_ands])
