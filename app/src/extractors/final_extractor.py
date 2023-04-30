from app.src.extractors.value_extractor import IExtractValue

from app.classes.custom_event.custom_event import CustomEvent

# This is where we may want to add the contract in
## For example, to verify that it's a legitimate obligation 
# TODO: Will need to find a way to handle dates/timepoints, etc
# e.g. may have FinalEventNode, or FinalDateNode for example...
# That makes sense actually. Add it when it comes up
class FinalExtractor(IExtractValue[any]):    
    def extract(self, str_val: str) -> any:
        return CustomEvent()
