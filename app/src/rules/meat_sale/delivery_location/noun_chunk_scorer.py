from typing import List, Tuple
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff


class NounChunkScorer(IScoreStuff):
    def __init__(
        self, 
        nlp
    ):
        self.__nlp = nlp
    
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        results = []

        for nc in list(req.doc.noun_chunks):
            start_ind = 0
            if nc[0].pos_ == 'DET':
                start_ind = 1
            next_nc = nc[start_ind:].text
            next_score = 0.1 # Should come from options

            results.append((next_nc, next_score))

        return results
