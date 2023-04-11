from app.classes.tokens.abstract_node import DummyNode
from app.classes.tokens.root_node import RootNode

class TestGrammar:
    @staticmethod
    def get_grammar() -> RootNode:
        l12c = [DummyNode('121'), DummyNode('122'), DummyNode('123')]
        l12 = DummyNode('12', l12c)

        l11c = [DummyNode('111'), DummyNode('112')]
        l11 = DummyNode('11', l11c)

        root_node = RootNode('Root', [l11, l12])
        return root_node