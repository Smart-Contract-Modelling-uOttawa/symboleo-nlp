from typing import List, Type, Dict
from app.classes.contract_update_request import ContractUpdateRequest
from app.classes.processing.components import Parameter
from app.classes.processing.scored_components import ScoredParameter, ScoredComponent
from app.src.rules.contract_spec.all_primitives_scorer import IScoreAllPrimitives
from app.src.rules.contract_spec.recursive_identifier import IIdentifyParametersRecursively

class IScoreParameters:
    def score(self, req: ContractUpdateRequest) -> List[ScoredParameter]:
        raise NotImplementedError()

class ParameterScorer(IScoreParameters):
    def __init__(
        self, 
        primitive_scorer: IScoreAllPrimitives,
        parm_types: List[Type[Parameter]],
        recursive_identifier: IIdentifyParametersRecursively,
        defaults: List[Parameter] = [] 
    ):
        self.__parm_types = parm_types
        self.__primitive_scorer = primitive_scorer 
        self.__recursive_identifier = recursive_identifier
        self.__defaults = defaults

    
    def score(self, req: ContractUpdateRequest) -> List[ScoredParameter]:
        results = []

        # May pull this out
        scored_components: List[ScoredComponent] = self.__primitive_scorer.score(req)
        scored_components.extend([ScoredComponent(x, 1) for x in self.__defaults])
        
        for p_type in self.__parm_types:
            next_result = self.__recursive_identifier.identify(p_type, scored_components)
            if next_result:
                results.append(next_result)
        
        return results
    