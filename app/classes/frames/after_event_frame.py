from app.classes.frames.frame import Frame
from app.classes.grammar.node_type import NodeType
from app.src.operations.configs import OpCode

class AfterEventFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.AFTER, NodeType.EVENT]
    op_code = OpCode.REFINE_PREDICATE
    subject: str = ''
    verb: str = ''

    def is_complete(self):
        return self.subject != '' and self.verb != '' 

    def to_text(self):
        # Will add NLP in here to ensure verb tense, etc
        return f'after {self.subject} is {self.verb}'
    