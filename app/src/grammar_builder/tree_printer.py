from app.classes.grammar.grammar_node import GrammarNode

class TreePrinter:
    def print(self, root_node: GrammarNode):
        self.rec_print(root_node)

    def rec_print(self, node: GrammarNode, i = 0):
        indent = '-' * i
        print(f'{indent} {node.name}')
        if not node.children:
            return
        
        for x in node.children:
            self.rec_print(x, i+1)