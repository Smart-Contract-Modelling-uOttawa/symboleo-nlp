from typing import Dict
from app.classes.domain_model.domain_model import DomainProp
from app.src.rules.domain_model.similarity_scorer import IScoreSimilarity

class IScoreProperySimilarity:
    def get_scores(self, props: list[DomainProp], doc) -> Dict[str, float]:
        raise NotImplementedError()


class PropertySimilarityScorer(IScoreProperySimilarity):
    def __init__(
        self, 
        nlp, 
        similarity_scorer: IScoreSimilarity
    ):
        self.__nlp = nlp
        self.__similarity_scorer = similarity_scorer
    
    # I may need to rework this a bit
    ## It might be desirable to concatenate in the event name that is in question
    ## E.g. instead of comparing "the amount owed" with just "amount", we could compare it with "amount paid"
    ## with "paid" being the name of the event.
    ## Would need to restructure. May just need to pass in events... then I can also prepend the event name to the result piece
    ## I could also sort the scores here...
    def get_scores(self, props: list[DomainProp], span) -> Dict[str, float]:
        result = {}

        for x in props:
            dk = self.__nlp(x.key)
            sk = self.__similarity_scorer.score(dk, span)

            dv = self.__nlp(x.value)
            sv = self.__similarity_scorer.score(dv, span)

            result[x.key] = max(sk,sv)
        
        return result