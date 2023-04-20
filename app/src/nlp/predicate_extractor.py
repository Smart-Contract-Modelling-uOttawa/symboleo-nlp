from app.classes.other.predicate import Predicate

class IExtractPredicate:
    def extract(self, pred_str: str) -> Predicate:
        raise NotImplementedError()


class PredicateExtractor:    
    def __init__(self):
        self.__nlp = None

    def extract(self, pred_str: str) -> Predicate:
        return Predicate(pred_str)
