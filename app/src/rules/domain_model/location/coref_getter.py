from spacy.matcher import Matcher
from spacy.tokens.doc import Doc
from typing import Dict,List

class IGetCorefs:
    def get(self, doc:Doc, base_ind: int, full_doc:Doc) -> Dict[int, List]:
        raise NotImplementedError()


class CorefGetter(IGetCorefs):
    def __init__(self, nlp):
        self.__nlp = nlp


    def get(self, doc:Doc, base_ind:int, full_doc:Doc) -> Dict[int, List]:
        # Find corefs in the short doc (e.g. their, its, etc...)
        coref_matcher = Matcher(self.__nlp.vocab)
        coref_pattern = [
            [{ "POS": "PRON", "DEP": 'poss' }]
        ]
        coref_matcher.add('coref', coref_pattern)
        coref_matches = coref_matcher(doc)

        # Get the start indices of each match
        target_indices = [start for _, start, _ in coref_matches]
        result = dict.fromkeys(target_indices, [])

        # For each match index (form short doc), search the extracted corefs in the full doc
        for target_ind in target_indices:
            full_ind = base_ind + target_ind
            next_res = self._process_for_index(full_ind, full_doc)
            result[target_ind] = next_res
        
        return result


    def _process_for_index(self, full_ind, full_doc):
        for coref in full_doc._.coref_chains:
            for mention in coref.mentions:
                #print(m)
                if full_ind in mention:
                    # Found -> find all the other mentions
                    next_res = [full_doc[ind].text.lower() for mm in coref.mentions for ind in mm]
                    return next_res
        return []