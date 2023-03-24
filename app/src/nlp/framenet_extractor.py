from typing import Dict, List
import nltk
from nltk.corpus.reader.framenet import FramenetCorpusReader, AttrDict, PrettyDict

class IExtractFrameFromVerb:
    def extract_flus_from_verb(self, verb: str) -> List[AttrDict]:
        raise NotImplementedError()
    
    def extract_core_fes(self, frame: AttrDict) -> Dict[str, AttrDict]:
        raise NotImplementedError()
    
    
class FramenetExtractor(IExtractFrameFromVerb):
    def __init__(self, fn: FramenetCorpusReader):
        #nltk.download('framenet_v17')
        self.__fn = fn


    def extract_flus_from_verb(self, verb: str) -> List[AttrDict]:
        regex_string = r'^' + verb
        frame_lus = self.__fn.lus(regex_string)
        verb_flus = [f for f in frame_lus if f.POS == 'V']
        return verb_flus


    def extract_core_fes(self, frame: AttrDict) -> Dict[str, AttrDict]:
        all_fes: PrettyDict = frame.FE
        core_keys = [k for k in all_fes if all_fes[k].coreType == 'Core']
        target_fes = {k: all_fes[k] for k in core_keys}
        return target_fes