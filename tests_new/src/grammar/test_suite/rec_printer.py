class RecursivePrinter:
    def print_it(self, root_node):
        print(root_node.id)
        self.rec_print(root_node, 0)

    def rec_print(self, node, i):
        ds = '--'*i
        for c in node.children:
            print(f'{ds} {c.id}')
            self.rec_print(c, i+1)