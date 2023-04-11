from app.classes.spec.proposition import Proposition, PNegAtom, PAnd, PComparison, PEquality
from app.classes.spec.p_atoms import PredicateFunction, PAtomPredicateTrueLiteral, PAtomPredicateFalseLiteral, PAtomPredicate
from app.classes.spec.other_predicates import PredicateFunctionCannotBeAssigned

# Convenience methods for creating Propositions
class PropMaker:
    @staticmethod
    def make(p: PredicateFunction, negation: bool = False) -> Proposition:
        return Proposition(
            p_ands = [PAnd(
                p_eqs= [PEquality(
                    curr = PComparison(
                        PNegAtom(
                            PAtomPredicate(p),
                            negation = negation
                        )
                    )
                )]
            )]
        )

    def make_default(value:bool = True) -> Proposition:
        atom = PAtomPredicateTrueLiteral() if value else PAtomPredicateFalseLiteral()
        
        return Proposition(
            p_ands = [PAnd(
                p_eqs= [PEquality(
                    curr = PComparison(
                        PNegAtom(
                            atom = atom,
                            negation = False
                        )
                    )
                )]
            )]
        )

    def make_not_assigned(arg: str) -> Proposition:
        return Proposition(
            p_ands = [PAnd(
                p_eqs= [PEquality(
                    curr = PComparison(
                        curr = PNegAtom(
                            atom = PredicateFunctionCannotBeAssigned(arg)
                        )
                    )
                )]
            )]
        )
