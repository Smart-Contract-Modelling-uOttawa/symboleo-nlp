import simple_cache
from typing import List

from app.classes.operations.user_input import UnitType, UserInput

class InputStorage:
    def __init__(self):
        self.__ttl = 20000
        self.__cache_name = 'user_input.cache'

    def init_input(self, unique_key):
        self._save(unique_key, [])


    def add_input(self, unique_key:str, user_input: UserInput):
        curr = self._load(unique_key)
        curr.append(user_input)
        self._save(unique_key, curr)


    def get_final(self, unique_key) -> List[UserInput]:
        curr_elements = self._load(unique_key)
        return curr_elements


    def _save(self, unique_key:str, elements: List[UserInput]):
        cache_id = f'{unique_key}.user_input'
        simple_cache.save_key(self.__cache_name, cache_id, elements, self.__ttl)


    def _load(self, unique_key:str) -> List[UserInput]:
        cache_id = f'{unique_key}.user_input'
        elements: List[UserInput] = simple_cache.load_key(self.__cache_name, cache_id)
        return elements