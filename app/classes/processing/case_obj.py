class CaseObj:
    args = None # List of primitives
    pred = None

    def __init__(self, args, pred):
        self.args = args
        self.pred = pred

class CasePattern:
    pattern = None
    pred = None

    def __init__(self, pattern, pred):
        self.pattern = pattern
        self.pred = pred