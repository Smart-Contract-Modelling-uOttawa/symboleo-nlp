from typing import List, Tuple
from nltk.tree import *
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff
from app.src.rules.domain_model.domain_event_prop_scorer import IScoreDomainEventProps
from app.src.matcher_helper import MyMatcher

# Extraction: X % of domain prop
# This could still be broken up a little bit more
class PercentScorer(IScoreStuff):
    def __init__(
        self,
        nlp,
        matcher: MyMatcher,
        domain_event_prop_scorer: IScoreDomainEventProps
    ):
        self.__nlp = nlp
        self.__matcher = matcher
        self.__domain_event_prop_scorer = domain_event_prop_scorer


    # May need to wrap in a try-catch that returns a 0
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        # Validate and get the match of the initial piece
        pattern = [
            [{"POS": "NUM", "TAG": "CD", "IS_SENT_START": True }, {"LOWER": "%"}, {"LOWER": "of"} ],
        ]
        match = self.__matcher.match(pattern, req.doc)
        if match is None:
            return []

        # Extract the remainder of the text
        next_start_ind = match[-1].i + 5
        end_text = req.doc.text[next_start_ind:]
        end_doc = self.__nlp(end_text)

        # Extract first component (e.g. 10%)... Might prefer to get something like 0.10...
        num_component = f'{req.doc[0].text}{req.doc[1].text}' 

        # Enforce that the remaining text is a NP
        if not self._validate_parse(end_doc):
            return []

        # Get scores for the domain model events
        # Looking to see if any events have domain props that match the request value
        inner_scores = self.__domain_event_prop_scorer.score(req.contract.domain_model.events, req.doc)
        
        # Combine the % with the found domain prop
        results = [(f'{num_component} * {s[0]}', s[1]) for s in inner_scores]

        return results


    # Move to Static function?
    def _validate_parse(self, doc):
        sent = list(doc.sents)[0]
        tree = Tree.fromstring(sent._.parse_string) 
        if tree.label() != 'NP':
            return False
        
        return True
