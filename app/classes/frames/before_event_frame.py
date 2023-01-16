from app.classes.frames.frame import Frame
from app.classes.grammar.node_type import NodeType

class BeforeEventFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.BEFORE, NodeType.EVENT]
    subject: str = ''
    verb: str = ''

    def to_text(self):
        # Will add NLP in here to ensure verb tense, etc
        return f'before {self.subject} is {self.verb}'


class BeforeDateFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.BEFORE, NodeType.DATE]
    date_text: str = ''

    def to_text(self):
        return f'before {self.date_text}'


class WithinTimespanEventFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.WITHIN, NodeType.TIMESPAN, NodeType.EVENT]
    timespan: str = ''
    subject: str = ''
    verb: str = ''

    def to_text(self):
        return f'within {self.timespan} of {self.subject} being {self.verb}'



    
