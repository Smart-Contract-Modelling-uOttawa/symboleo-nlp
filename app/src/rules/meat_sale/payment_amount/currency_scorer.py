from typing import List, Tuple
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff

class CurrencyScorer(IScoreStuff):
    def __init__(
        self, 
        allowed_values: List[str]
    ):
        self.__allowed_values = [s.lower() for s in allowed_values]
        # e.g. [CAD, USD] ## This comes from domain model
        ## May be injected into the nlp pipeline at the start
        ## We may not want to overwrite the entity name recognizer. Since there is a good chance it will recognize MONEY
    
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        scores = []

        contains_money = 'MONEY' in [x.label_ for x in req.doc.ents]
        contains_symbol = '$' in [x.text for x in req.doc]

        for t in req.doc:
            t_score = 0 

            if t.text.lower() in self.__allowed_values:
                t_score += 0.5

                if t.ent_type == 'MONEY':
                    t_score += 0.4
                elif contains_money:
                    t_score += 0.1
                
                if contains_symbol:
                    t_score += 0.1
            
            if t_score > 0:
                scores.append((t.text, t_score))

        return scores

