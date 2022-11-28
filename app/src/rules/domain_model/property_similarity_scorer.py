from typing import Dict
from app.classes.domain_model.domain_model import DomainProp


class IScoreProperySimilarity:
    def get_scores(self, props: list[DomainProp], doc) -> Dict[str, float]:
        raise NotImplementedError()


class PropertySimilarityScorer(IScoreProperySimilarity):
    def __init__(self, nlp):
        self.__nlp = nlp
    
    # I may need to rework this a bit
    ## It might be desirable to concatenate in the event name that is in question
    ## E.g. instead of comparing "the amount owed" with just "amount", we could compare it with "amount paid"
    ## with "paid" being the name of the event.
    ## Would need to restructure. May just need to pass in events... then I can also prepend the event name to the result piece
    ## I could also sort the scores here...
    def get_scores(self, props: list[DomainProp], doc) -> Dict[str, float]:
        result = {}

        for x in props:
            dk = self.__nlp(x.key)
            sk = dk.similarity(doc)

            dv = self.__nlp(x.value)
            sv = dv.similarity(doc)

            result[x.key] = sk*sv
        
        return result