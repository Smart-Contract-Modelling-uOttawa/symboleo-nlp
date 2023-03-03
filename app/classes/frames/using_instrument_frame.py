from app.classes.frames.frame import Frame
from app.classes.grammar.node_type import NodeType
from app.src.operations.configs import OpCode

class UsingInstrumentFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.USING, NodeType.INSTRUMENT]
    op_code = OpCode.ADD_DM_PROP
    instrument: str = ''

    def is_complete(self):
        return self.instrument != '' 

    def to_text(self):
        # Will add NLP in here...
        return f'using {self.instrument}'
