from typing import List, Tuple
from nltk.tree import *
from spacy.matcher import Matcher
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff
from app.src.rules.domain_model.property_similarity_scorer import IScoreProperySimilarity


class PercentScorer(IScoreStuff):
    def __init__(
        self,
        nlp,
        property_similarity_scorer: IScoreProperySimilarity
    ):
        self.__nlp = nlp
        self.__prop_scorer = property_similarity_scorer


    # MAy need to wrap in a try-catch that returns a 0
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        # Validate and get the match of the initial piece
        match = self._get_single_match(req.doc)

        if match is None:
            return []

        # Extract the remainder of the text
        end_ind = match[2]
        next_start_ind = end_ind + len('of') + 2
        end_text = req.doc.text[next_start_ind:]
        end_doc = self.__nlp(end_text)

        # Extract first component (e.g. 10%)
        ## TODO: Might prefer to get something like 0.10...
        num_component = f'{req.doc[0].text}{req.doc[1].text}' 

        # Enforce that the remaining text is a NP
        if not self._validate_parse(end_doc):
            return []

        # Get scores for the domain model events
        domain_events = req.contract.domain_model.events     
        all_scores = self._get_scores_from_dm_dict(domain_events, end_doc)

        sorted_scores = sorted(all_scores, key=lambda x: x[1], reverse=True)
        # Add a correction to the score
        corrected_scores = [self._correct_score(score) for score in sorted_scores]
        results = [(f'{num_component} * {s[0]}', s[1]) for s in corrected_scores]

        return results

    def _correct_score(self, score):
        correction = 0.5
        return (score[0], score[1] + correction)

    def _get_scores_from_dm_dict(self, dm_dict, doc):
        results = []
        for key in dm_dict:
            evt = dm_dict[key]
            next_scores = self.__prop_scorer.get_scores(evt.props, doc)
            
            for ns in next_scores:
                results.append((f'{key}.{ns}', next_scores[ns]))
        
        return results


    def _validate_parse(self, doc):
        sent = list(doc.sents)[0]
        tree = Tree.fromstring(sent._.parse_string) 
        if tree.label() != 'NP':
            return False
        
        return True


    def _get_single_match(self, doc):
        new_matcher = Matcher(self.__nlp.vocab)
        start_pattern = [
            [{"TAG": "CD", "IS_SENT_START": True }, {"LOWER": "%"}, {"LOWER": "of"} ],
        ]
        new_matcher.add('start', start_pattern)

        matches = new_matcher(doc)

        if len(matches) != 1:
            return None
        
        return matches[0]