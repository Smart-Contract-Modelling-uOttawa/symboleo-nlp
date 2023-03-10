from app.classes.spec.proposition import PNegAtom, Proposition
from app.classes.spec.contract_spec import Norm

class IExtractNegations:
    def extract(self, norm: Norm, component: str) -> bool:
        raise NotImplementedError()

class NegationExtractor(IExtractNegations):
    def extract(self, norm: Norm, component: str) -> bool:
        result = False

        proposition: Proposition = norm.__dict__[component]

        # If its non-empty
        try:
            pneg: PNegAtom = proposition.p_ands[0].p_eqs[0].curr.curr
            result = pneg.negation 
        except Exception as e:
            result = False

        return result