from typing import List 
from app.classes.other.helpers import ClassHelpers

class NounPhrase:
    def __init__(
        self, 
        str_val:str, 
        head:str, 
        is_plural: bool = False,
        is_role: bool = False,
        det: str = None, 
        adjs: List[str] = None
    ):
        self.str_val = str_val
        self.head = head
        self.is_plural = is_plural
        self.is_role = is_role
        self.det = det
        self.adjs = adjs


    def __eq__(self, __value: object) -> bool:
        return self.str_val == __value.str_val and \
        self.head == __value.head and \
        self.is_plural == __value.is_plural and \
        self.is_role == __value.is_role and \
        self.det == __value.det and \
        ClassHelpers.simple_lists_eq(self.adjs, __value.adjs)
        

    # TODO: Will likely add more types - might make an enum: basic, original, full
    def to_text(self, type='basic'):
        result = self.head
        if self.adjs and len(self.adjs) > 0:
            result = f'{self.adjs[-1]} {result}'

        return result