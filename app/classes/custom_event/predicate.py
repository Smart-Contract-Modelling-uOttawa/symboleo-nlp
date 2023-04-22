class Predicate:
    # Potential properties: Number of words, categories
    def __init__(
        self, 
        pred_str: str,
    ):
        self.pred_str = pred_str
    
    def to_text(self):
        return self.pred_str
    

    