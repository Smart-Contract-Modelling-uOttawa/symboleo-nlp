from typing import List 

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


    # TODO: Will likely add more types - might make an enum: basic, original, full
    def to_text(self, type='basic'):
        result = self.head
        if self.adjs and len(self.adjs) > 0:
            result = f'{self.adjs[-1]} {result}'

        return result