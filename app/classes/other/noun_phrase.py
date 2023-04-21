from typing import List 

# May have a special flag to denote if the subject is a role...
class NounPhrase:
    def __init__(
        self, 
        str_val:str, 
        head:str, 
        is_plural: bool = False,
        is_role: bool = False,
        is_asset: bool = False,
        det: str = None, 
        adjs: List[str] = None
    ):
        self.str_val = str_val
        self.head = head
        self.is_plural = is_plural
        self.is_role = is_role
        self.is_asset = is_asset
        self.det = det
        self.adjs = adjs
    
    def print_me(self):
        print(f'Head: {self.head}')
        print(f'adjs: {self.adjs}')
        print(f'is plural: {self.is_plural}')
        print(f'det: {self.det}')


    # types: basic, head, original - make this an enum...
    def to_text(self, type='basic'):
        result = self.head
        if self.adjs and len(self.adjs) > 0:
            result = f'{self.adjs[-1]} {result}'

        return result