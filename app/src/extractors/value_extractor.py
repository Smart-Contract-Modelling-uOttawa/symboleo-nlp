from typing import DefaultDict
from collections import defaultdict
from app.classes.tokens.node_type import *

from app.src.nlp.verb.verb_extractor_builder import VerbExtractorBuilder
from app.src.nlp.subject_extractor import SubjectExtractor
from app.src.nlp.adverb.adverb_extractor import AdverbExtractor
from app.src.nlp.predicate_extractor import PredicateExtractor
from app.src.nlp.dobj_extractor import DobjectExtractor
from app.src.nlp.prep_phrase_extractor import PrepPhraseExtractor

from app.src.operations.dependencies import Dependencies

# Might make this generic [T]
class IExtractValue:
    def extract(self, str_val: str):
        raise NotImplementedError()
    
class DefaultExtractor(IExtractValue):
    def extract(self, str_val: str):
        return str_val

class ValueExtractorDictBuilder:
    @staticmethod
    def build(deps: Dependencies) -> DefaultDict[NodeType, IExtractValue]:
        
        subject_extractor = SubjectExtractor(deps.nlp)
        verb_extractor = VerbExtractorBuilder.build(deps.nlp)
        dobj_extractor = DobjectExtractor(deps.nlp)
        predicate_extractor = PredicateExtractor()
        adverb_extractor = AdverbExtractor()
        pp_extractor = PrepPhraseExtractor(deps.nlp)

        d = defaultdict(lambda: DefaultExtractor())

        d[NodeType.SUBJECT] = subject_extractor
        d[NodeType.VERB] = verb_extractor
        d[NodeType.PREP_PHRASE] = pp_extractor
        d[NodeType.ADVERB] = adverb_extractor
        d[NodeType.DOBJ] = dobj_extractor
        d[NodeType.PREDICATE] = predicate_extractor
        
        d[NodeType.CONTRACT_SUBJECT] = subject_extractor
        d[NodeType.CONTRACT_ACTION] = verb_extractor
        ##...
        

        return d


