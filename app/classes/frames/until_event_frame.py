from app.classes.frames.frame import Frame
from app.classes.grammar.node_type import NodeType
from app.src.operations.configs import OpCode

class UntilEventFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.UNTIL, NodeType.EVENT]
    op_code = OpCode.ADD_NORM
    subject: str = ''
    verb: str = ''

    def is_complete(self):
        return self.subject != '' and self.verb != '' 

    def to_text(self):
        # Will add NLP in here to ensure verb tense, etc
        return f'until {self.subject} has been {self.verb}'