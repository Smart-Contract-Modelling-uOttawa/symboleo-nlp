from typing import List,Dict
from app.src.rules.shared.interfaces import IProcessDocs

class ILookupProcessor:
    def lookup(self, key: str) -> List[IProcessDocs]:
        raise NotImplementedError()
    

class ProcessorLookup(ILookupProcessor):
    def __init__(self, processor_dict: Dict[str, List[IProcessDocs]]):
        self.__dict = processor_dict
    
    def lookup(self, key: str) -> List[IProcessDocs]:
        if key in self.__dict:
            return self.__dict[key]
        else:
            raise NotImplementedError(f'Missing processor for key: {key}')
