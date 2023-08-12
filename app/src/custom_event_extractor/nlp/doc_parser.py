from typing import List

class DocUnit:
    def __init__(self, text:str, tag:str, dep:str, head:str):
        self.text = text
        self.tag = tag
        self.dep = dep 
        self.head = head
    
class NlpDoc:
    def __init__(self, tokens: List[DocUnit]):
        self.tokens = tokens
    
    def print_me(self):
        print('\n')
        for x in self.tokens:
            print(x.text)
            print(x.tag)
            print(x.dep)
            print(x.head)


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
