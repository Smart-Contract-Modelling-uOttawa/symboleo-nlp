from app.classes.tokens.node_type import *

class UserInput:
    def __init__(self, node_type:NodeType, value: str = None):
        self.node_type = node_type
        self.value = value
        