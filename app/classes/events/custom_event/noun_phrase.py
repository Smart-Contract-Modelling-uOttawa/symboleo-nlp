from __future__ import annotations
from enum import Enum
from typing import List 
from app.classes.helpers.list_eq import ClassHelpers

class NPTextType(Enum):
    ORIGINAL = 'original',
    HEAD = 'head'
    BASIC = 'basic'

class NounPhrase:
    def __init__(
        self, 
        str_val:str, 
        head:str, 
        is_plural: bool = False,
        is_role: bool = False,
        det: str = None, 
        adjs: List[str] = None,
        asset_type: str = None,
        is_parm = False,
        asset_id = None
    ):
        self.str_val = str_val
        self.head = head
        self.is_plural = is_plural
        self.is_role = is_role
        self.det = det
        self.adjs = adjs
        self.asset_type = asset_type
        self.is_parm = is_parm
        self.asset_id = asset_id
        if self.adjs is None:
            self.adjs = []


    def __eq__(self, other: NounPhrase) -> bool:
        return self.str_val == other.str_val and \
            self.head == other.head and \
            self.is_plural == other.is_plural and \
            self.is_role == other.is_role and \
            self.det == other.det and \
            self.asset_type == other.asset_type and \
            self.is_parm == other.is_parm and \
            self.asset_id == other.asset_id and \
            ClassHelpers.simple_lists_eq(self.adjs, other.adjs)
        
    def print_me(self): # pragma: no cover
        print(f'- {self.str_val}')
        print(f'- {self.head}')
        print(f'- {self.is_plural}')
        print(f'- {self.is_role}')
        print(f'- {self.det}')
        print(f'- {self.asset_type}')
        print(f'- {self.is_parm}')
        print(f'- {self.asset_id}')
        print(f'- {self.adjs}')


    def to_text(self, text_type: NPTextType = NPTextType.ORIGINAL):
        if text_type == NPTextType.ORIGINAL:
            return self.str_val
        elif text_type == NPTextType.HEAD:
            return self.head
        else: # BASIC
            result = self.head
            if self.adjs and len(self.adjs) > 0:
                result = f'{self.adjs[-1]} {result}'
            return result