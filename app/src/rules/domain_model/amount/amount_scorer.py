from typing import List, Tuple
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff

# Goal is to extract a number... look for numbers
## Can incorporate some more intelligent spacy matchers in here for validation or extraction

class AmountScorer(IScoreStuff):
    def __init__(
        self,
        nlp
    ):
        self.__nlp = nlp
    
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        scores = []

        contains_money = 'MONEY' in [x.label_ for x in req.doc.ents]
        contains_symbol = '$' in [x.text for x in req.doc] 
        # Pattern: $ Num

        for t in req.doc:
            t_score = 0 

            if t.pos_ == 'NUM':
                t_score += 0.5

                if t.ent_type == 'MONEY':
                    t_score += 0.4
                elif contains_money:
                    t_score += 0.1

                if contains_symbol:
                    t_score += 0.1

            if t_score > 0:
                scores.append((t.text, t_score))

        print('SCORES', scores)
        return scores

