from typing import DefaultDict
from collections import defaultdict
from app.classes.tokens.node_type import *

from app.src.extractors.custom_event.verb.verb_extractor_builder import VerbExtractorBuilder
from app.src.extractors.custom_event.noun_phrase_extractor import NounPhraseExtractor
from app.src.extractors.custom_event.fake_noun_phrase_extractor import FakeNounPhraseExtractor
from app.src.extractors.custom_event.adverb_extractor import AdverbExtractor
from app.src.extractors.custom_event.predicate_extractor import PredicateExtractor
from app.src.extractors.custom_event.prep_phrase_extractor import PrepPhraseExtractor

from app.src.extractors.contract_action_extractor import ContractActionExtractor
from app.src.extractors.obligation_action_extractor import ObligationActionExtractor
from app.src.extractors.obligation_subject_extractor import ObligationSubjectExtractor

from app.classes.operations.dependencies import Dependencies

# TODO: Need to strongly type the extractors - may use a generic [T]
## May also need to bring in the contract as input
class IExtractValue:
    def extract(self, str_val: str):
        raise NotImplementedError()
    
class DefaultExtractor(IExtractValue):
    def extract(self, str_val: str):
        return str_val

class ValueExtractorDictBuilder:
    @staticmethod
    def build(deps: Dependencies) -> DefaultDict[NodeType, IExtractValue]:
        
        if deps.fake:
            np_extractor = FakeNounPhraseExtractor()
        else:
            np_extractor = NounPhraseExtractor(deps.nlp)
    
        verb_extractor = VerbExtractorBuilder.build(deps.nlp, deps.fake)
        predicate_extractor = PredicateExtractor()
        adverb_extractor = AdverbExtractor()
        pp_extractor = PrepPhraseExtractor(deps.nlp, np_extractor)

        d = defaultdict(lambda: DefaultExtractor())

        d[NodeType.SUBJECT] = np_extractor
        d[NodeType.VERB] = verb_extractor
        d[NodeType.PREP_PHRASE] = pp_extractor
        d[NodeType.ADVERB] = adverb_extractor
        d[NodeType.DOBJ] = np_extractor
        d[NodeType.PREDICATE] = predicate_extractor
        
        d[NodeType.CONTRACT_ACTION] = ContractActionExtractor() 

        d[NodeType.OBLIGATION_ACTION] = ObligationActionExtractor() 
        d[NodeType.OBLIGATION_SUBJECT] = ObligationSubjectExtractor() 
        ##...
        
        return d
