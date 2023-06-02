class Predicate:
    # Potential properties: Number of words, categories
    def __init__(
        self, 
        pred_str: str,
    ):
        self.pred_str = pred_str
    
    def __eq__(self, __value: object) -> bool:
        return self.pred_str == __value.pred_str

    def to_text(self):
        return self.pred_str
    

    