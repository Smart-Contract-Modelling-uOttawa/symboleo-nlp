class IGetLabels:
    def get(self, str_val: str) -> str:
        raise NotImplementedError()

class LabelGetter(IGetLabels):
    def __init__(self, nlp) -> None:
        self.__nlp = nlp
    
    def get(self, str_val: str) -> str:
        result = None
        
        doc = self.__nlp(str_val)

        if len(doc.ents) > 0:
            result = doc.ents[0].label_
        
        return result