from app.classes.frames.frame import Frame
from app.classes.grammar.node_type import NodeType
from app.src.operations.parm_configs import ParmOpCode

# TODO: May remove this one...
class UsingInstrumentFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.USING, NodeType.INSTRUMENT]
    op_code = ParmOpCode.ADD_DM_PROP
    instrument: str = ''

    def is_complete(self):
        return self.instrument != '' 

    def to_text(self):
        # Will add NLP in here...
        return f'using {self.instrument}'
