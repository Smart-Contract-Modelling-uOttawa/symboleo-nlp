from app.classes.frames.frame import Frame
from app.classes.grammar.node_type import NodeType
from app.src.operations.parm_operations.parameter_updater import ParmOpCode

class IfEventFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.IF, NodeType.EVENT]
    op_code = ParmOpCode.ADD_TRIGGER
    subject: str = ''
    verb: str = ''

    def is_complete(self):
        return self.subject != '' and self.verb != '' 

    def to_text(self):
        # Will add NLP in here to ensure verb tense, etc
        # Will need lots of processing here... Depends on type of verb, etc.
        
        return f'if {self.subject} has been {self.verb}'
