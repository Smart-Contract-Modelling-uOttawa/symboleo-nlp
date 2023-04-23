from app.classes.template_event.obligation_subject import ObligationSubject
from app.src.extractors.value_extractor import IExtractValue

# TODO: These need to inherit from the extractor interface
class ObligationSubjectExtractor(IExtractValue[ObligationSubject]):    
    def extract(self, str_val: str) -> ObligationSubject:
        return ObligationSubject(str_val)
