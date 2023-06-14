import simple_cache
from typing import List

from app.classes.elements.element import Element
from app.classes.elements.static_elements import RootElement, FinalElement

class InputStorage:
    def __init__(self):
        self.__ttl = 20000
        self.__cache_name = 'elements.cache'

    def init_input(self, unique_key):
        init_elements = [RootElement()]
        self._save(unique_key, init_elements)


    def add_input(self, unique_key:str, element: Element):
        curr_elements = self._load(unique_key)
        curr_elements.append(element)
        self._save(unique_key, curr_elements)


    def get_final(self, unique_key) -> List[Element]:
        curr_elements = self._load(unique_key)
        curr_elements.append(FinalElement())
        return curr_elements


    def _save(self, unique_key:str, elements: List[Element]):
        cache_id = f'{unique_key}.elements'
        simple_cache.save_key(self.__cache_name, cache_id, elements, self.__ttl)


    def _load(self, unique_key:str) -> List[Element]:
        cache_id = f'{unique_key}.elements'
        elements: List[Element] = simple_cache.load_key(self.__cache_name, cache_id)
        return elements