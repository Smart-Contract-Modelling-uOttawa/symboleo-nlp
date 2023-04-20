from enum import Enum
from typing import List

class AdverbType(Enum):
    TIME = 'time',
    FREQUENCY = 'frequency',
    PLACE = 'place',
    MANNER = 'manner',
    DEGREE = 'degree',
    REASON = 'reason',
    RELATIVE = 'relative',
    ATTITUDE = 'attitude'


class Adverb:
    # Potential properties: Number of words, categories
    def __init__(
        self, 
        adverb_str: str,
        adverb_types: List[AdverbType] = None
    ):
        self.adverb_str = adverb_str
        self.adverb_types = adverb_types
    
    def to_text(self):
        return self.adverb_str
    

    