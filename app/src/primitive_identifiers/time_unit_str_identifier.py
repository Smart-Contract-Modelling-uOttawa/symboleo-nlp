from app.classes.spec.helpers import TimeUnitStr
from app.classes.spec.primitive import ScoredPrimitive
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives

class TimeUnitStrIdentifier(IIdentifyPrimitives):
    def __init__(
        self, 
    ):
        self.__dict = {
            'seconds': ['seconds', 'second'],
            'minutes': ['minutes', 'minute'],
            'hours': ['hours', 'hour'],
            'days': ['days', 'day'],
            'weeks': ['weeks', 'week'],
            'months': ['months', 'month'],
            'years': ['years', 'year']
        }
        unit_lists = list(self.__dict.values())
        self.__all_units = [item for sublist in unit_lists for item in sublist]


    def identify(self, doc) -> ScoredPrimitive:
        target1 = [x for x in doc if x.text.lower() in self.__all_units]

        target2 = [x for x in target1 if x.ent_type_ in ['TIME', 'DATE']]

        if len(target2) > 0:
            primitive_text = self._pluralize(target2[0].text)
            score = 1
        elif len(target1) > 0:
            primitive_text = self._pluralize(target1[0].text)
            score = 0.5
        else:
            primitive_text = ''
            score = 0
        
        return ScoredPrimitive(TimeUnitStr(primitive_text), score)


    def _pluralize(self, x):
        for k in self.__dict:
            if x in self.__dict[k]:
                return k
        
        return ''
    
