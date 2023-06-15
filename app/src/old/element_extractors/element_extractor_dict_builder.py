
from collections import defaultdict
from typing import DefaultDict
from mlconjug3 import Conjugator as ML3Conjugator

from app.classes.operations.dependencies import Dependencies
from app.classes.units.unit_type import UnitType

from app.src.element_extractors.verb.lemmatizer import Lemmatizer
from app.src.element_extractors.verb.fake_lemmatizer import FakeLemmatizer
from app.src.element_extractors.verb.conjugator import MyConjugator
from app.src.element_extractors.verb.verb_extractor import VerbExtractor
from app.src.selection.element_extractors.contract_action_extractor import ContractActionExtractor
from app.src.element_extractors.adverb_extractor import AdverbExtractor
from app.src.element_extractors.noun_phrase.fake_noun_phrase_extractor import FakeNounPhraseExtractor
from app.src.element_extractors.noun_phrase.noun_phrase_extractor import NounPhraseExtractor
from app.src.element_extractors.predicate_extractor import PredicateExtractor
from app.src.element_extractors.prep_phrase_extractor import PrepPhraseExtractor
from app.src.selection.element_extractors.obligation_action_extractor import ObligationActionExtractor
from app.src.selection.element_extractors.obligation_subject_extractor import ObligationSubjectExtractor
from app.src.selection.element_extractors.contract_subject_extractor import ContractSubjectExtractor
from app.src.selection.element_extractors.final_extractor import FinalExtractor
from app.src.selection.element_extractors.timespan_extractor import TimespanExtractor
from app.src.element_extractors.element_extractor import DefaultExtractor, IExtractElement

from app.src.element_extractors.noun_phrase.asset_type_extractor import AssetTypeExtractor


class ElementExtractorDictBuilder:
    @staticmethod
    def build(deps: Dependencies) -> DefaultDict[UnitType, IExtractElement]:
        

        if deps.fake:
            np_extractor = FakeNounPhraseExtractor()
        else:
            asset_type_extractor = AssetTypeExtractor(deps.nlp)
            np_extractor = NounPhraseExtractor(deps.nlp, asset_type_extractor)

        inner_conjugator = ML3Conjugator(language = 'en')
        if deps.fake:
            lemmatizer = FakeLemmatizer()
        else:
            lemmatizer = Lemmatizer(deps.nlp)

        conjugator = MyConjugator(inner_conjugator)
        verb_extractor = VerbExtractor(lemmatizer, conjugator)
        predicate_extractor = PredicateExtractor()
        adverb_extractor = AdverbExtractor()
        pp_extractor = PrepPhraseExtractor(deps.nlp, np_extractor)

        d = defaultdict(lambda: DefaultExtractor())

        d[UnitType.SUBJECT] = np_extractor
        d[UnitType.VERB] = verb_extractor
        d[UnitType.PREP_PHRASE] = pp_extractor
        d[UnitType.ADVERB] = adverb_extractor
        d[UnitType.DOBJ] = np_extractor
        d[UnitType.PREDICATE] = predicate_extractor

        d[UnitType.CONTRACT_SUBJECT] = ContractSubjectExtractor()
        d[UnitType.CONTRACT_ACTION] = ContractActionExtractor(lemmatizer)
        d[UnitType.OBLIGATION_ACTION] = ObligationActionExtractor()
        d[UnitType.OBLIGATION_SUBJECT] = ObligationSubjectExtractor()
        
        d[UnitType.TIMESPAN] = TimespanExtractor()

        #d[UnitType.FINAL_NODE] = FinalExtractor()

        return d