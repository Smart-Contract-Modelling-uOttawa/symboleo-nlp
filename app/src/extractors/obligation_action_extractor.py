from app.classes.spec.sym_event import ObligationEventName

# TODO: These need to inherit from the extractor interface
class ObligationActionExtractor:    
    def extract(self, str_val: str) -> ObligationEventName:
        return ObligationEventName[str_val.capitalize()]
