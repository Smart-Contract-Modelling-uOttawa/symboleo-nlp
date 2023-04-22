from app.classes.template_event.obligation_subject import ObligationSubject

# TODO: These need to inherit from the extractor interface
class ObligationSubjectExtractor:    
    def extract(self, str_val: str) -> ObligationSubject:
        return ObligationSubject(str_val)
