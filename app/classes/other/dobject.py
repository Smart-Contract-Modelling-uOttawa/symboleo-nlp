from typing import List 

# May have a special flag to denote if the subject is a role...
class DObject:
    def __init__(self, dobj_str: str, head:str, is_plural: bool, det: str = None, adjs: List[str] = None):
        self.subj_str = dobj_str
        self.head = head
        self.is_plural = is_plural
        self.det = det
        self.adjs = adjs
    
    def print_me(self):
        print(f'Head: {self.head}')
        print(f'adjs: {self.adjs}')
        print(f'is plural: {self.is_plural}')
        print(f'det: {self.det}')


    def to_text(self):
        result = self.head
        if self.adjs and len(self.adjs) > 0:
            result = f'{self.adjs[-1]} {result}'

        return result