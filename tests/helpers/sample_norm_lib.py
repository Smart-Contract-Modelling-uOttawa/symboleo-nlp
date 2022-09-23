from app.classes.spec.atoms import EventProposition
from app.classes.spec.helpers import Point, SymEvent
from app.classes.spec.symboleo_spec import Junction, NegAtom, Norm, Obligation, Proposition, Role

class SampleNorms:

    @staticmethod
    def get_sample_norm() -> Norm:
        return Obligation(
            'O1',
            None,
            Role('Seller'),
            Role('Buyer'),
            None,
            Proposition([
                Junction([
                    NegAtom(
                        EventProposition(
                            SymEvent('delivered'),
                            Point('BEFORE delivered.delDueD')
                        )
                    )
                ])
            ])
       )