from typing import List, Tuple
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff

# Goal is to extract a number... look for numbers
## Can incorporate some more intelligent spacy matchers in here for validation or extraction

class SimpleAmountScorer(IScoreStuff):
    def __init__(
        self,
        nlp
    ):
        self.__nlp = nlp
        self.__currencies = ['CAD', 'USD'] # May want to pass this in...
    
    # Handles simple cases - only one dollar value mentioned
    ## Can add other scorers to handle more difficult cases later on
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        scores = []

        nums = [x.text for x in req.doc if x.pos_ == 'NUM']
        money_ents = [x.text for x in req.doc.ents if x.label_ == 'MONEY']
        symbol = [x.text for x in req.doc if x.text == '$']
        currencies = [x.text for x in req.doc if x.text in self.__currencies]

        # TODO: Would like to incorporate dependencies in as well

        # TODO: For these validations, I may rig them to throw message errors, then just catch them
        ## Would allow us to transmit valuable info back to the user
        # Simple Validation. Ensure not more than one for each piece
        if len(nums) != 1 or len(money_ents) > 1 or len(symbol) > 1 or len(currencies) > 1:
            return scores
        
        # If ONLY a number, then not enough info
        if (len(money_ents) == 0 and len(symbol) == 0 and len(currencies) == 0):
            return scores

        # If doc is too long
        if len(req.doc) > 10:
            return scores

        score = len(nums)*0.5 + len(money_ents)*0.4 + len(symbol)*0.2 + len(currencies)*0.2  

        score = min(score, 1)

        if score > 0:
            scores.append((nums[0], score))

        return scores

