from __future__ import annotations

class Predicate:
    # Potential properties: Number of words, categories
    def __init__(self, pred_str: str,):
        self.pred_str = pred_str
    
    def __eq__(self, __value: Predicate) -> bool:
        return self.pred_str == __value.pred_str
