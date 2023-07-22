import unittest
from unittest.mock import MagicMock

from app.classes.grammar.grammar_node import GrammarNode
from app.src.grammar_builder.tree_merger import TreeMerger
from app.src.grammar_builder.tree_printer import TreePrinter

class TreeMergerTests(unittest.TestCase):
    def setUp(self):
        self.sut = TreeMerger()

    def test_tree_merger1(self):
        t1 = GrammarNode('ROOT')

        t2 = GrammarNode('A', [
            GrammarNode('B', [
                GrammarNode('C'),
            ])
        ])

        exp_value = GrammarNode('ROOT', [
            GrammarNode('A', [
                GrammarNode('B', [
                    GrammarNode('C')    
                ]),  
            ])
        ])

        self.sut.merge(t1, t2)
        
        self.assertEqual(t1, exp_value)


    def test_tree_merger2(self):
        t1 = GrammarNode('A', [
            GrammarNode('B', [
                GrammarNode('C'),
            ]),
            GrammarNode('D', [
                GrammarNode('E'),
            ]),
        ])

        t2 = GrammarNode('B', [
            GrammarNode('F'),
        ])

        exp_value = GrammarNode('A', [
            GrammarNode('B', [
                GrammarNode('C'),
                GrammarNode('F')
            ]),
            GrammarNode('D', [
                GrammarNode('E')
            ])
        ])

        self.sut.merge(t1, t2)

        self.assertEqual(t1, exp_value)

    def test_tree_merger3(self):
        t1 = GrammarNode('ROOT', [
            GrammarNode('A', [
                GrammarNode('B'),
            ]),
            GrammarNode('C', [
                GrammarNode('D'),
                GrammarNode('E'),
            ]),
        ])

        t2 = GrammarNode('C', [
            GrammarNode('D', [
                GrammarNode('H'),
                GrammarNode('I')
            ]),
            GrammarNode('E', [
                GrammarNode('F'),
            ])
        ])

        exp_value = GrammarNode('ROOT', [
            GrammarNode('A', [
                GrammarNode('B')
            ]),
            GrammarNode('C', [
                GrammarNode('D', [
                    GrammarNode('H'),
                    GrammarNode('I')
                ]),
                GrammarNode('E', [
                    GrammarNode('F')
                ])
            ])
        ])

        self.sut.merge(t1, t2)

        self.assertEqual(t1, exp_value)


if __name__ == '__main__':
    unittest.main()
