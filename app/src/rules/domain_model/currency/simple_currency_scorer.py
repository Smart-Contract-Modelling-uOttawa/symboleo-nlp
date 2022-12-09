from typing import List, Tuple
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff

class SimpleCurrencyScorer(IScoreStuff):
    def __init__(
        self, 
        currencies: List[str]
    ):
        self.__currencies = [s.lower() for s in currencies]
        # e.g. [CAD, USD] ## This comes from domain model
        ## May be injected into the nlp pipeline at the start
        ## We may not want to overwrite the entity name recognizer. Since there is a good chance it will recognize MONEY
    
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        scores = []

        # Extract the expected components
        nums = [x.text for x in req.doc if x.pos_ == 'NUM']
        money_ents = [x.text for x in req.doc.ents if x.label_ == 'MONEY']
        symbol = [x.text for x in req.doc if x.text == '$']
        currencies = [x.text for x in req.doc if x.text.lower() in self.__currencies]

        # Validation: 
        if len(currencies) == 0:
            return scores
        
        # Ensure not more than one for each piece
        if len(nums) != 1 or len(money_ents) > 1 or len(symbol) > 1 or len(currencies) > 1:
            return scores
        
        # If ONLY a number, then not enough info
        if (len(money_ents) == 0 and len(symbol) == 0 and len(currencies) == 0):
            return scores

        # If doc is too long
        if len(req.doc) > 10:
            return scores

        score = len(currencies)*0.5 + len(money_ents)*0.4 + len(symbol)*0.1 + len(nums)*0.1  

        score = min(score, 1)

        if score > 0:
            scores.append((currencies[0], score))

        return scores

