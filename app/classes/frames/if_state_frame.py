from app.classes.frames.frame import Frame
from app.classes.grammar.node_type import NodeType

class IfStateFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.IF, NodeType.STATE]
    subject: str = ''
    verb: str = ''

    def is_complete(self):
        return self.subject != '' and self.verb != '' 

    def to_text(self):
        # Will add NLP in here to ensure verb tense, etc
        return f'if {self.subject} has been {self.verb}'