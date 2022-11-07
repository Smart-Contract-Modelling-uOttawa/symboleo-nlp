# should inherit from some common class
from app.classes.spec.predicate_function import PredicateFunctionHappensAfter, PredicateFunctionWHappensBefore
from app.classes.spec.sym_point import Point, PointAtomParameterDotExpression, PointFunction, PointAtomContractEvent
from app.classes.spec.sym_event import ContractEvent
from app.classes.spec.helpers import TimeUnitStr, TimeValueInt, VariableDotExpression
from app.src.dynamic_constructor import IConstructDynamicObjects
from app.src.rules.shared.helpers import RuleHelpers

# Goal: have this fully configured and dynamic

# within_time_period
# before_date
# after_date
# before_event
# after_event
# between_date_and_date
# within_time_period_of_event
## https://7esl.com/prepositions-of-time/

class CaseObj:
    args = None # List of primitives
    pred = None

    def __init__(self, args, pred):
        self.args = args
        self.pred = pred


class DeliveryTimeframeProcessor:
    def __init__(
        self, 
        template, 
        matcher, 
        nlp,
        dynamic_constructor: IConstructDynamicObjects
    ):
        self.__template = template
        self.__matcher = matcher
        self.__nlp = nlp
        self.__case_dict = {
            'within_time_period': CaseObj([PointFunction], PredicateFunctionWHappensBefore),
            'before_date': CaseObj([PointAtomParameterDotExpression], PredicateFunctionWHappensBefore),
            'after_date': CaseObj([PointAtomParameterDotExpression], PredicateFunctionHappensAfter),
            'before_event': CaseObj([None], None),
            'after_event': CaseObj([None], None),
            'between_date_and_date': CaseObj([None], None),
            'within_time_period_of_event': CaseObj([None], None)
        }

        self.__dynamic_constructor = dynamic_constructor

        # Can maybe just do this for all primitives... just loop through them
        ## May also pass in some default primitives as well...
        ## Need the template too
        self.__primitive_dict = {
            'time_value_int': TimeValueInt,
            'time_unit_string': TimeUnitStr,
            'point_vde': VariableDotExpression
        }
        

    def process(self, doc):
        # Check for PP.. Replace with another matcher
        ## Generalize this to some rules that are passed in
        ## Essentially I want to generalize everything and reduce these to config files
        is_pp = RuleHelpers.is_pp(doc)
        if not is_pp:
            raise 'Missing prepositional phrase'
        
        # Get the matches
        matches = self.__matcher(doc)

        # print('matches:')
        # for m_id, start, end in matches:
        #     print('-', self.__nlp.vocab.strings[m_id], doc[start:end])

        # Find out which scenario we are in
        case_matches = self._get_case_matches(matches, doc)
        # print('case matches:', case_matches)
        
        # Extract all the primitives
        ## I dont want to use a dict in the constructor - want a generic one for all of them - cleaner
        primitives = self._get_primitives(matches, doc)

        # Add in the default... This may cause an issue later on. Needs some justification
        ## May just want to pass this one in to the constructor...
        ## Also, these arent necessarily primitives - they are the building blocks
        contract_event = ContractEvent('activated')
        pace = PointAtomContractEvent(contract_event)
        primitives.append(pace)

        # print('primitives:')
        # for p in primitives:
        #     print('-', type(p), p.to_sym())
        
        results = []

        # Build a predicate result for each matching case we find
        for key in case_matches:
            case_obj = self.__case_dict[key]
            next_result = self._build_next_result(primitives, case_obj)
            results.append(next_result)
        
        return results

    

    def _build_next_result(self, primitives, caseObj: CaseObj):
        needed_args = caseObj.args

        # May be a problem to have multiple needed_args - since the primitives will be used multiple times. - not good
        arg_set = []
        for target_type in needed_args:
            next_arg = self.__dynamic_constructor.construct(target_type.__name__, primitives)
            arg_set.append(next_arg)
        
        # Add the relevant template pieces
        for template_arg in self.__template.__dict__:
            next_arg = self.__template.__dict__[template_arg]
            arg_set.append(next_arg)
        
        # Construct it
        target_type = caseObj.pred
        next_result = self.__dynamic_constructor.construct(target_type.__name__, arg_set)
        
        return next_result



    def _get_primitives(self, matches, doc):
        primitives = []
        for x in self.__primitive_dict:
            next_val = self._extract_max(matches, x) # Not all will be found. Need to wrap with error-handling
            if next_val:
                next_span = doc[next_val[1]:next_val[2]]
                next_primitive = self.__primitive_dict[x](next_span)
                primitives.append(next_primitive)
        
        return primitives



    def _get_case_matches(self, matches, doc):
        case_matches = {}
        for x in self.__case_dict:
            next_val = self._extract_max(matches, x)
            if next_val:
                next_span = doc[next_val[1]:next_val[2]]
                case_matches[x] = next_span

        return case_matches
        

    def _extract_max(self, matches, k):
        all_matches = [x for x in matches if self.__nlp.vocab.strings[x[0]] == k]
        if len(all_matches) > 0:
            return max(all_matches, key=lambda x: x[2]-x[1])
        else:
            return None

