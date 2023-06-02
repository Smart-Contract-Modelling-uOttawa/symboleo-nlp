from typing import Dict, List
from app.src.nlp.framenet import IFramenet, MyLU, MyFrame, MyFrameElement

class IExtractFrameFromVerb:
    def extract_flus_from_verb(self, verb: str) -> List[MyLU]:
        raise NotImplementedError()

    def extract_core_fes(self, frame: MyFrame) -> Dict[str, MyFrame]:
        raise NotImplementedError()
    
    
class FramenetExtractor(IExtractFrameFromVerb):
    def __init__(self, fn: IFramenet):
        self.__fn = fn

    def extract_flus_from_verb(self, verb: str) -> List[MyLU]:
        regex_string = r'^' + verb
        frame_lus = self.__fn.get_lus(regex_string)
        verb_flus = [f for f in frame_lus if f.pos == 'V']
        return verb_flus


    def extract_core_fes(self, frame: MyFrame) -> Dict[str, MyFrameElement]:
        all_fes = frame.frame_elements
        core_keys = [k for k in all_fes if all_fes[k].type == 'Core']
        target_fes = {k: all_fes[k] for k in core_keys}
        return target_fes