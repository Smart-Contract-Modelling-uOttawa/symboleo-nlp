import copy
from app.classes.spec.proposition import PNegAtom, Proposition, PAnd, PEquality, PComparison
from app.classes.spec.contract_spec import Norm
from app.classes.spec.p_atoms import PAtomPredicateFalseLiteral, PAtomPredicateTrueLiteral

class IUpdateNormPropositions:
    def update(self, norm: Norm, str_component: str, new_atom: PNegAtom) -> Norm:
        raise NotImplementedError()

# TODO: Can we assume that we're replacing and not appending?? May need a flag argument
class NormPropositionUpdater(IUpdateNormPropositions):
    def update(self, norm: Norm, str_component: str, new_atom: PNegAtom) -> Norm:
        new_norm = copy.deepcopy(norm)
        component: Proposition = getattr(new_norm, str_component)

        # If it doesn't have a predicate, then create it
        new_p_and = PAnd([PEquality(PComparison(new_atom))])

        # If non-existent, then create it
        if type(component) in [PAtomPredicateTrueLiteral, PAtomPredicateFalseLiteral]:
            component = Proposition(p_ands = [ PAnd([]) ])
            component.p_ands.append(new_p_and)
        
        # If one already exists, then need the PAnd
        else:
            #component.p_ands.append(new_p_and) # Appends;
            component.p_ands = [new_p_and] # Replaces; rather than appends. May need a flag argument...
            
        setattr(new_norm, str_component, component)

        return new_norm

