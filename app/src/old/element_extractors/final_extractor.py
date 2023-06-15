from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.element_extractors.element_extractor import IExtractElement
from app.classes.events.custom_event.custom_event import CustomEvent

# TODO: B2 - Need to figure out the purpose of this. It will likely break
# e.g. may have FinalEventNode, or FinalDateNode for example...
# That makes sense actually. Add it when it comes up
class FinalExtractor(IExtractElement[any]):    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> any:
        return CustomEvent()
