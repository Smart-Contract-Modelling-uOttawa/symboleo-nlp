import copy
from app.classes.spec.symboleo_spec import Norm, PNegAtom, Proposition, PAnd, PEquality, PComparison

class IUpdateNormPropositions:
    def update(self, norm: Norm, str_component: str, new_atom: PNegAtom) -> Norm:
        raise NotImplementedError()


class NormPropositionUpdater(IUpdateNormPropositions):
    def update(self, norm: Norm, str_component: str, new_atom: PNegAtom) -> Norm:
        new_norm = copy.deepcopy(norm)
        component: Proposition = getattr(new_norm, str_component)


        # If non-existent, then create it
        if component == None:
            component = Proposition([PAnd([PEquality([PComparison([

            ])])])])
            component.p_ands[0].p_eqs[0].p_comps[0].p_atoms.append(new_atom)
        
        # If one already exists, then need the PAnd
        elif len(component.p_ands) > 0:
            new_p_and = PAnd([PEquality([PComparison([
                new_atom
            ])])])
            component.p_ands.append(new_p_and)
            
        setattr(new_norm, str_component, component)

        return new_norm
    
