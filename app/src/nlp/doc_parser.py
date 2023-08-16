from app.classes.events.doc_unit import DocUnit, NlpDoc

class IParseDoc:
    def parse(self, str_val:str) -> NlpDoc:
        raise NotImplementedError

class DocParser(IParseDoc):
    def __init__(self, nlp):
        self.__nlp = nlp

    def parse(self, str_val: str) -> NlpDoc:
        doc = self.__nlp(str_val)
        doc_units = [] 
        for x in doc:
            next_unit = DocUnit(x.text, x.tag_, x.dep_, x.head.text)
            doc_units.append(next_unit)
        
        return NlpDoc(doc_units)
