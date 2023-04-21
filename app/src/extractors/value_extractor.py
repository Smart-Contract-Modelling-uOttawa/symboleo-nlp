from typing import DefaultDict
from collections import defaultdict
from app.classes.tokens.node_type import *

from app.src.nlp.verb.verb_extractor_builder import VerbExtractorBuilder
from app.src.nlp.noun_phrase_extractor import NounPhraseExtractor
from app.src.nlp.adverb.adverb_extractor import AdverbExtractor
from app.src.nlp.predicate_extractor import PredicateExtractor
from app.src.nlp.prep_phrase_extractor import PrepPhraseExtractor

from app.src.operations.dependencies import Dependencies

# Might make this generic [T]
# I Haven't actually strongly-typed the extractors yet
# I may also bring in the contract as an input... could be optional
## Useful for checking if something like a subject is a role
class IExtractValue:
    def extract(self, str_val: str):
        raise NotImplementedError()
    
class DefaultExtractor(IExtractValue):
    def extract(self, str_val: str):
        return str_val

class ValueExtractorDictBuilder:
    @staticmethod
    def build(deps: Dependencies) -> DefaultDict[NodeType, IExtractValue]:
    
        np_extractor = NounPhraseExtractor(deps.nlp)
        verb_extractor = VerbExtractorBuilder.build(deps.nlp)
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
        
        d[NodeType.CONTRACT_SUBJECT] = np_extractor
        d[NodeType.CONTRACT_ACTION] = verb_extractor
        ##...
        

        return d


