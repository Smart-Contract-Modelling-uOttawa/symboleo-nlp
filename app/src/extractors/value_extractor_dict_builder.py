from collections import defaultdict
from typing import DefaultDict

from app.classes.operations.dependencies import Dependencies
from app.classes.units.unit_type import UnitType
from app.src.extractors.contract_action_extractor import ContractActionExtractor
from app.src.extractors.custom_event.adverb_extractor import AdverbExtractor
from app.src.extractors.custom_event.noun_phrase.fake_noun_phrase_extractor import FakeNounPhraseExtractor
from app.src.extractors.custom_event.noun_phrase.noun_phrase_extractor import NounPhraseExtractor
from app.src.extractors.custom_event.predicate_extractor import PredicateExtractor
from app.src.extractors.custom_event.prep_phrase_extractor import PrepPhraseExtractor
from app.src.extractors.custom_event.verb.verb_extractor_builder import VerbExtractorBuilder
from app.src.extractors.obligation_action_extractor import ObligationActionExtractor
from app.src.extractors.obligation_subject_extractor import ObligationSubjectExtractor
from app.src.extractors.common_event_extractor import CommonEventExtractor
from app.src.extractors.contract_subject_extractor import ContractSubjectExtractor
from app.src.extractors.final_extractor import FinalExtractor
from app.src.extractors.timespan_extractor import TimespanExtractor
from app.src.extractors.value_extractor import DefaultExtractor, IExtractValue

from app.src.extractors.custom_event.noun_phrase.asset_type_extractor import AssetTypeExtractor


class ValueExtractorDictBuilder:
    @staticmethod
    def build(deps: Dependencies) -> DefaultDict[UnitType, IExtractValue]:
        

        if deps.fake:
            np_extractor = FakeNounPhraseExtractor()
        else:
            asset_type_extractor = AssetTypeExtractor(deps.nlp)
            np_extractor = NounPhraseExtractor(deps.nlp, asset_type_extractor)

        verb_extractor = VerbExtractorBuilder.build(deps.nlp, deps.fake)
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
        d[UnitType.CONTRACT_ACTION] = ContractActionExtractor()
        d[UnitType.OBLIGATION_ACTION] = ObligationActionExtractor()
        d[UnitType.OBLIGATION_SUBJECT] = ObligationSubjectExtractor()
        
        d[UnitType.COMMON_EVENT] = CommonEventExtractor()

        d[UnitType.TIMESPAN] = TimespanExtractor()

        #d[UnitType.FINAL_NODE] = FinalExtractor()

        return d