from app.classes.frames.frame import Frame
from app.classes.tokens.node_type import NodeType
from app.src.operations.parm_configs import ParmOpCode

class BeforeEventFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.BEFORE, NodeType.EVENT]
    op_code = ParmOpCode.REFINE_PREDICATE
    subject: str = ''
    verb: str = ''

    def is_complete(self):
        return self.subject != '' and self.verb != '' 

    def to_text(self):
        # Will add NLP in here to ensure verb tense, etc
        return f'before {self.subject} is {self.verb}'
    