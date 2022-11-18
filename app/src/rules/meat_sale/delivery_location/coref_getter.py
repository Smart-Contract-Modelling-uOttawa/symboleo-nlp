from spacy.matcher import Matcher

class IGetCorefs:
    def get(self, doc, key: str, template_string: str):
        raise NotImplementedError()


class CorefGetter(IGetCorefs):
    def __init__(self, nlp):
        self.__nlp = nlp

    def get(self, doc, key: str, template_string: str):
        base_ind = self._get_base_ind(template_string, key)
        full_string = template_string.replace(f'[{key}]', doc.text)
        full_doc = self.__nlp(full_string)

        coref_matcher = Matcher(self.__nlp.vocab)
        coref_pattern = [
            [{ "POS": "PRON", "DEP": 'poss' }]
        ]
        coref_matcher.add('coref', coref_pattern)

        # Match up the text between doc and full_doc
        coref_matches = coref_matcher(doc)
        
        target_indices = [start for _, start, _ in coref_matches]

        result = dict.fromkeys(target_indices, [])

        for target_ind in target_indices:
            full_ind = base_ind + target_ind
            next_res = self._process_for_index(full_ind, full_doc)
            result[target_ind] = next_res
        
        return result
    
    def _get_base_ind(self, template_string, key):
        upto_ind = template_string.index(f'[{key}]')
        upto_str = template_string[:upto_ind]
        upto_doc = self.__nlp(upto_str)
        base_ind = len(upto_doc)
        return base_ind


    def _process_for_index(self, full_ind, full_doc):
        for coref in full_doc._.coref_chains:
            for mention in coref.mentions:
                #print(m)
                if full_ind in mention:
                    # Found -> find all the other mentions
                    next_res = [full_doc[ind].text.lower() for mm in coref.mentions for ind in mm]
                    return next_res
        return []