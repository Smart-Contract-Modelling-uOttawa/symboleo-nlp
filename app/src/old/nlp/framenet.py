from typing import List, Dict
from nltk.corpus.reader.framenet import FramenetCorpusReader, AttrDict, PrettyDict


class MyFrameElement:
    def __init__(self, fn_fe: AttrDict = None, name:str = None, defn: str = None, type:str = None):
        self.name = name or fn_fe.name
        self.definition = defn or fn_fe.definition
        self.type = type or fn_fe.coreType

class MyFrame:
    def __init__(self, fn_frame: AttrDict = None, frame_elements:Dict[str,MyFrameElement] = None):
        self.frame_elements: Dict[str, MyFrameElement] = frame_elements or {}
        if not frame_elements:
            for x in fn_frame.FE:
                self.frame_elements[x] = MyFrameElement(fn_frame.FE[x])

class MyLU:
    def __init__(self, fn_lu:AttrDict = None, pos:str = None, name:str = None, defn:str = None, frame:MyFrame = None):
        self.pos = pos or fn_lu.POS
        self.name = name or fn_lu.name
        self.definition = defn or fn_lu.definition
        self.frame: MyFrame = frame or MyFrame(fn_lu.frame)

# Interface for framenet
class IFramenet:
    def get_lus(self, regex_string) -> List[MyLU]:
        raise NotImplementedError()        


class MyFramenet(IFramenet):
    def __init__(self, base_fn: FramenetCorpusReader):
        self.__fn = base_fn
    

    def get_lus(self, regex_string) -> List[MyLU]:
        fn_result = self.__fn.lus(regex_string)
        result = [MyLU(x) for x in fn_result]
        return result