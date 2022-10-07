from app.classes.spec.symboleo_spec import Obligation
from app.src.atom_extractor import IExtractAtoms
from app.src.norm_proposition_updater import IUpdateNormPropositions

class IConvertSentenceToObligation:
    def convert(self, sentence: str, obligation: Obligation, selected_component: str) -> Obligation:
        raise NotImplementedError()

class SentenceObligationConverter(IConvertSentenceToObligation):
    def __init__(
        self, 
        atom_extractor: IExtractAtoms,
        norm_updater: IUpdateNormPropositions
    ):
        self.__atom_extractor = atom_extractor
        self.__norm_updater = norm_updater

    def convert(self, sentence: str, obligation: Obligation, selected_component: str) -> Obligation:
        atoms = self.__atom_extractor.extract(sentence)

        if len(atoms) > 0:
            result = self.__norm_updater.update(obligation, selected_component, atoms[0])
            return result

        # No matches found => invalid entry
        raise ValueError()
