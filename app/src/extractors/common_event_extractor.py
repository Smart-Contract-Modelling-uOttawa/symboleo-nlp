from app.classes.template_event.common_event import CommonEvent
from app.src.extractors.value_extractor import IExtractValue

from app.classes.template_event.common_event_dict import COMMON_EVENT_DICT

class CommonEventExtractor(IExtractValue[CommonEvent]):    
    def extract(self, str_val: str) -> CommonEvent:
        return COMMON_EVENT_DICT[str_val]
