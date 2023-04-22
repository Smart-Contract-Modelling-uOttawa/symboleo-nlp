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
    

# These were generated using ChatGPT (Limitation) - not perfect
class AdverbDict:
    adverb_type_dict = {
        AdverbType.TIME: ['yesterday', 'today', 'tomorrow', 'now', 'soon', 'later', 'early', 'late', 'before', 'after', 'already'],
        AdverbType.FREQUENCY: ["always", "constantly", "continuously", "often", "frequently", "usually", "normally", "generally", "regularly", "routinely", "sometimes", "occasionally", "intermittently", "sporadically", "infrequently", "rarely", "seldom", "hardly ever", "almost never", "never"],
        AdverbType.PLACE: ['above', 'below', 'here', 'there', 'nearby', 'faraway', 'upstairs', 'downstairs', 'inside', 'outside', 'abroad', 'everywhere', 'anywhere', 'nowhere', 'somewhere', 'behind', 'in front', 'around', 'away', 'aside'],
        AdverbType.MANNER: ['knowingly', 'intentionally', 'willfully', 'fraudulently', 'maliciously', 'negligently', 'recklessly', 'carelessly', 'consciously', 'deliberately', 'purposely', 'systematically', 'diligently', 'exclusively', 'expressly', 'implicitly', 'materially', 'mutually', 'jointly', 'severally', 'irrevocably', 'conditionally', 'unconditionally'],
        AdverbType.DEGREE: ["absolutely", "accurately", "adequately", "completely", "conclusively", "definitely", "entirely", "exclusively", "expressly", "fully", "generally", "independently", "individually", "necessarily", "particularly", "precisely", "principally", "purely", "quite", "reasonably", "solely", "specifically", "strictly", "substantially", "totally", "unconditionally", "uniquely", "utterly", "wholly", "widely"],
        AdverbType.REASON: ['accordingly', 'consequently', 'thus', 'therefore', 'hence', 'so', 'for this reason', 'as a result', 'due to this', 'as such', 'as a consequence', 'resultantly', 'in consequence', 'because of this', 'owing to this', 'on account of this', 'by reason of this', 'in view of this', 'with the result that', 'in this way', 'in this manner', 'by virtue of this', 'for that reason', 'in light of this', 'under these circumstances', 'given these facts', 'in consideration of this', 'in consequence of this', 'as an outcome', 'resulting from this'],
        AdverbType.RELATIVE: ['where', 'wherein', 'whereas', 'whereby', 'whereupon', 'whereof', 'thereby', 'therefore', 'therefrom', 'thereto', 'hereby', 'herein', 'hereof', 'hereto', 'hereunder', 'hereafter', 'hereinbefore', 'aforesaid', 'above-mentioned', 'aforementioned', 'above-referenced', 'above-described', 'aforedescribed', 'as', 'so', 'as if', 'as though', 'as per', 'as of', 'as from'],
        AdverbType.ATTITUDE: ['expressly', 'specifically', 'clearly', 'unequivocally', 'absolutely', 'definitely', 'positively', 'categorically', 'unequivocally', 'conclusively', 'undeniably', 'indisputably', 'irrefutably', 'unconditionally', 'completely','entirely', 'fully', 'wholly', 'thoroughly', 'exclusively', 'solely', 'merely','simply', 'purely', 'strictly', 'absolutely', 'definitely', 'certainly', 'truly', 'genuinely'],
    }


    