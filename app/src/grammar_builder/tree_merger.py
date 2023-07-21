from app.classes.grammar.grammar_node import GrammarNode
        
class IMergeTrees:
    def merge(self, curr: GrammarNode, x: GrammarNode, i = 0) -> GrammarNode:
        raise NotImplementedError()


class TreeMerger(IMergeTrees):
    def merge(self, curr: GrammarNode, x: GrammarNode, i = 0):
        # Find the root of next_tree in the curr_tree
        target_node = self._rec_find(curr, x)

        # If not found, then append as children
        if not target_node:
            curr.children.append(x)
        else:
            # If found, recursively merge
            for c in x.children:
                self.merge(target_node, c, i+1)
        
    

    def _rec_find(self, curr: GrammarNode, target: GrammarNode, i=0) -> GrammarNode:
        if target.name == curr.name:
            return curr

        # New patterns should always be root children
        if i == 1:
            return None
        
        # Note that this is DFS... May want to do BFS
        for c in curr.children:
            next_res = self._rec_find(c, target, i+1)
            if next_res:
                return next_res
        
        return None