from app.src.matcher_helper import IGetMatches
from app.classes.spec.helpers import TimeUnitStr
from app.classes.spec.primitive import ScoredPrimitive
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives

class TimeUnitStrIdentifier(IIdentifyPrimitives):
    def __init__(
        self,
        matcher: IGetMatches
    ):
        self.__matcher = matcher
        
        ## Old stuff
        # self.__dict = {
        #     'seconds': ['seconds', 'second'],
        #     'minutes': ['minutes', 'minute'],
        #     'hours': ['hours', 'hour'],
        #     'days': ['days', 'day'],
        #     'weeks': ['weeks', 'week'],
        #     'months': ['months', 'month'],
        #     'years': ['years', 'year']
        # }
        # unit_lists = list(self.__dict.values())
        # self.__all_units = [item for sublist in unit_lists for item in sublist]

    def identify(self, doc) -> ScoredPrimitive:
        pattern = [
            [{"POS": "NOUN", "DEP": { "IN": ["pobj", "npadvmod", "dobj"]} , "ENT_TYPE": "DATE" }],
        ]
        match = self.__matcher.match(pattern, doc)

        if match:
            return ScoredPrimitive(TimeUnitStr(match.text), 1)
        
        return None


    ## Can hopefully get rid of all this... depends on testing performance 
    ## Assumption: Only taking the first time unit that is found...
    ## this is not a great assumption to make... e.g. "between 2 and 4 days" would be a problem
    def identify_old(self, doc) -> ScoredPrimitive:
        
        trigger_words = [x for x in doc if self._in_unit_list(x)]

        datetime_ents = [x for x in trigger_words if self._is_datetime_entity(x)]

        if len(datetime_ents) > 0:
            primitive_text = self._pluralize(datetime_ents[0].text)
            score = 1
        elif len(trigger_words) > 0:
            primitive_text = self._pluralize(trigger_words[0].text)
            score = 0.5
        else:
            primitive_text = ''
            score = 0
        
        return ScoredPrimitive(TimeUnitStr(primitive_text), score)


    def _in_unit_list(self, x): return x.text.lower() in self.__all_units

    def _is_datetime_entity(self, x): return x.ent_type_ in ['TIME', 'DATE']
    
    def _pluralize(self, x):
        for k in self.__dict:
            if x in self.__dict[k]:
                return k
        
        return ''
    
