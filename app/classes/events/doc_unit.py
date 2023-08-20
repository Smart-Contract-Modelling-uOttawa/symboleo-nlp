from __future__ import annotations
from typing import List

class DocUnit:
    def __init__(self, text:str, tag:str, dep:str, head:str):
        self.text = text
        self.tag = tag
        self.dep = dep 
        self.head = head
    
    def __eq__(self, other: DocUnit) -> bool:
        return self.text == other.text and \
            self.tag == other.tag and \
            self.dep == other.dep and \
            self.head == other.head

class NlpDoc:
    def __init__(self, tokens: List[DocUnit]):
        self.tokens = tokens
    
    def print_me(self): # pragma: no cover
        print('\n')
        for x in self.tokens:
            print('-----\n')
            print(f'- Text: {x.text}')
            print(f'- Tag: {x.tag}')
            print(f'- Dep: {x.dep}')
            print(f'- Head: {x.head}')
    
    def __eq__(self, other: NlpDoc) -> bool:
        return self.tokens == other.tokens