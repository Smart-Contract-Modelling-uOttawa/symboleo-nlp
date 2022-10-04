from app.classes.spec.symboleo_spec import PNegAtom
from app.src.atom_assembler import IAssembleAtoms
from app.src.primitive_extractor import IExtractPrimitives

class IExtractAtoms:
    def extract(self, text: str) -> list[PNegAtom]:
        raise NotImplementedError()
    
# Extract atoms from some text
class AtomExtractor(IExtractAtoms):
    def __init__(
        self,
        options, # dict?
        nlp,
        primitive_extractor: IExtractPrimitives,
        atom_assembler: IAssembleAtoms
    ):
        self.__options = options
        self.__nlp = nlp
        self.__primitive_extractor = primitive_extractor
        self.__atom_assembler = atom_assembler
        
    
    def extract(self, text: str) -> list[PNegAtom]:
        result: list[PNegAtom] = []
        doc = self.__nlp(text)

        # Extract the most likely primitives from the document
        primitives = self.__primitive_extractor.extract(doc)

        # Identify and assemble the main candidates
        result = self.__atom_assembler.assemble(primitives)

        return result