from app.classes.events.conj_type import ConjType

class BaseEvent:
    def to_sym_event(self):
        raise NotImplementedError()
    
    def to_text(conj_type:ConjType = ConjType.CONTINUOUS) -> str:
        raise NotImplementedError()

    def is_complete() -> bool:
        raise NotImplementedError()
    
