import copy
from app.classes.spec.symboleo_spec import Junction, NegAtom, Norm, Proposition

class IUpdateNorms:
    def update(self, norm: Norm, str_component: str, new_atom: NegAtom) -> Norm:
        raise NotImplementedError()


class NormUpdater(IUpdateNorms):
    def update(self, norm: Norm, str_component: str, new_atom: NegAtom) -> Norm:
        new_norm = copy.deepcopy(norm)
        component: Proposition = getattr(new_norm, str_component)

        # If non-existent, then create it
        if component == None:
            component = Proposition([
                Junction([])
            ])
            
        # If too many, then error
        if len(component.junctions) > 1:
            raise ValueError('Too many norm junctions')
        
        component.junctions[0].negAtoms.append(new_atom)

        setattr(new_norm, str_component, component)

        return new_norm
    
