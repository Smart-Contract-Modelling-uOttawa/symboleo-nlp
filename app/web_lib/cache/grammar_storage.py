import simple_cache
from app.classes.grammar.grammar_node import GrammarNode

class GrammarStorage:
    def __init__(self):
        self.__ttl = 20000
        self.__cache_name = 'grammar.cache'

    def store(self, unique_key:str, grammar_node: GrammarNode):
        simple_cache.save_key(self.__cache_name, f'{unique_key}', grammar_node, self.__ttl)
    

    def load(self, unique_key:str) -> GrammarNode:
        result: GrammarNode = simple_cache.load_key(self.__cache_name, f'{unique_key}')
        return result