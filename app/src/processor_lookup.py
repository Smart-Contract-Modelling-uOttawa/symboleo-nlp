from typing import Dict
from app.src.rules.shared.interfaces import IProcessDocs

class ILookupProcessor:
    def lookup(self, key: str) -> IProcessDocs:
        raise NotImplementedError()
    

class ProcessorLookup(ILookupProcessor):
    def __init__(self, processor_dict: Dict[str, IProcessDocs]):
        self.__dict = processor_dict
    
    def lookup(self, key: str) -> IProcessDocs:
        if key in self.__dict:
            return self.__dict[key]
        else:
            raise NotImplementedError(f'Missing processor for key: {key}')
