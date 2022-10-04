from app.classes.spec.symboleo_spec import PNegAtom
from app.src.predicate_builder import IBuildPredicates
from app.classes.spec.primitive import Primitive

# Should define a type for the primitives. Or maybe just a long OR thing...

class IAssembleAtoms:
    def assemble(self, primitives: list[Primitive]) -> list[PNegAtom]:
        raise NotImplementedError()

class AtomAssembler(IAssembleAtoms):
    def __init__(
        self,
        candidates: list[str],
        predicate_builder: IBuildPredicates
    ):
        self.__candidates = candidates
        self.__predicate_builder = predicate_builder

    def assemble(self, primitives: list[Primitive]) -> list[PNegAtom]:
        results = []
        for c in self.__candidates:
            next_result = self.__predicate_builder.build(c, primitives)
            if next_result:
                results.append(next_result)

        return results