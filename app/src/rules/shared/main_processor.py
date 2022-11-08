from app.src.dynamic_constructor import IConstructDynamicObjects
from app.src.rules.shared.i_config import IConfig
from app.src.rules.shared.case_obj import CaseObj

class MainProcessor:
    def __init__(
        self, 
        nlp,
        config: IConfig,
        dynamic_constructor: IConstructDynamicObjects
    ):
        self.__nlp = nlp
        self.__template = config.template
        self.__matcher = config.matcher
        self.__case_dict = config.case_dict
        self.__primitive_dict = config.primitive_dict
        self.__default_components = config.default_components
        self.__dynamic_constructor = dynamic_constructor


    def process(self, doc):        
        # Get the matches. Might even just pass these in 
        matches = self.__matcher(doc)

        # Find out which case we are in
        case_matches = self._get_case_matches(matches, doc)
        if len(case_matches) == 0:
            raise 'Invalid. No matching patterns'
        
        # Extract all the primitives
        primitives = self._get_primitives(matches, doc)
        # If none, then do something?
        
        # Build a predicate result for each matching case we find
        results = [
            self._build_next_result(primitives, self.__case_dict[k]) for k in case_matches 
        ]

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
                next_primitive = self.__primitive_dict[x](next_span.text)
                primitives.append(next_primitive)
        
        for x in self.__default_components:
            primitives.append(x)
        
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

