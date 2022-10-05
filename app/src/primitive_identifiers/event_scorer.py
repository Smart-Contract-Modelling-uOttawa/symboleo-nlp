
class IScoreEvents:
    def score(self, doc) -> tuple[str, float]:
        raise NotImplementedError()


class EventScorer(IScoreEvents):
    def __init__(self, dict_set):
        self.__dict_set = dict_set


    def score(self, doc) -> tuple[str, float]:
        root = [x for x in doc if x.dep_ == 'ROOT'][0]
        target_lemma = root.lemma_

        for d, score in self.__dict_set:
            d_check = self._find_dict_key(d, target_lemma)
            if d_check:
                return d_check, score
        
        return ('', 0)
    

    def _find_dict_key(self, d, w):
        for key in d:
            if w in d[key]:
                return key
        return None

    