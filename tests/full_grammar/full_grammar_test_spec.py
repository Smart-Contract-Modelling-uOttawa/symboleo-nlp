from typing import List
from app.classes.grammar.selected_node import SelectedNode

class FullGrammarTestSpec:
    def __init__(
            self, 
            selected_nodes: List[SelectedNode],
            exp_nl: str,
            exp_sym: str
        ):
            self.selected_nodes = selected_nodes
            self.exp_nl = exp_nl
            self.exp_sym = exp_sym

