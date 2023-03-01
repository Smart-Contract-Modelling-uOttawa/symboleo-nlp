from app.classes.frames.frame import Frame
from app.classes.grammar.node_type import NodeType
from app.src.operations.configs import OpCode


class BeforeEventFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.BEFORE, NodeType.EVENT]
    op_code = OpCode.REFINE_PREDICATE
    subject: str = ''
    verb: str = ''

    def is_complete(self):
        return self.subject != '' and self.verb != '' 

    def to_text(self):
        # Will add NLP in here to ensure verb tense, etc
        return f'before {self.subject} is {self.verb}'


class BeforeDateFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.BEFORE, NodeType.DATE]
    op_code = OpCode.REFINE_PREDICATE
    date_text: str = ''

    def is_complete(self):
        return self.date_text != ''

    def to_text(self):
        return f'before {self.date_text}'


class WithinTimespanEventFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.WITHIN, NodeType.TIMESPAN, NodeType.EVENT]
    op_code = OpCode.REFINE_PREDICATE
    timespan: str = ''
    subject: str = ''
    verb: str = ''

    def is_complete(self):
        return self.subject != '' and self.verb != '' and self.timespan != ''

    def to_text(self):
        return f'within {self.timespan} of {self.subject} being {self.verb}'


# class WhenEventFrame(Frame):
#     pattern = [NodeType.ROOT, NodeType.WHEN, NodeType.EVENT]
#     subject: str = ''
#     verb: str = ''

#     def to_text(self):
#         return f'when {self.subject} is {self.verb}'
    
