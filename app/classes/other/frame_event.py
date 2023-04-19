from __future__ import annotations
# TODO: Going to be spending LOTS of time on this...
class FrameEvent:
    # Add types to all of these
    subj = None
    verb = None
    adverb = None
    dobj = None
    predicate = None
    pps = []


    # Will likely be passing in conjugation information
    def to_text(self):
        return f'{self.subj} {self.verb} {self.dobj} {self.adverb}'


    def __eq__(self, other: FrameEvent) -> bool:
        if self.subj == other.subj and self.dobj == other.dobj and self.verb == other.verb:
            s1 = sorted(self.pps, key=lambda x: x.key)
            s2 = sorted(other.pps, key=lambda x: x.key)
            if len(s1) == len(s2):
                for i in range(len(s1)):
                    if s1[i] != s2[i]:
                        return False
                
                return True
        return False

    def is_complete(self):
        # Make this more complex
        return self.subj and self.verb

    def get_event_name(self): #Pascal case
        result = f'{self.verb.title()}' # PascalCase: VerbAdverb ?

        adverb: str = self.adverb
        if adverb:
            result += f'{adverb.title()}'\
        
        return result
