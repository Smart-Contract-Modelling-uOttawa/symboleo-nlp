from app.classes.contract_update_request import ContractUpdateRequest
from app.classes.processing.scored_components import ScoredPrimitive
from app.src.component_identifiers.interfaces import IScorePrimitives
from app.src.matcher_helper import IGetMatches

from app.classes.spec.sym_point import PointVDE


class PointVdeScorer(IScorePrimitives):
    def __init__(
        self,
        matcher: IGetMatches
    ):
        self.__matcher = matcher


    def score(self, req: ContractUpdateRequest) -> ScoredPrimitive:
        doc = req.doc
        pattern = [
            [{"POS": "PROPN", "DEP": "pobj" , "ENT_TYPE": "DATE" }, 
            {"POS": "NUM", "DEP": "nummod" , "ENT_TYPE": "DATE" },
            {"POS": "PUNCT", "DEP": "punct" , "ENT_TYPE": "DATE" },
            {"POS": "NUM", "DEP": "nummod" , "ENT_TYPE": "DATE" }],
        ]
        match = self.__matcher.match(pattern, doc)

        # Basically hard-coded... will need to handle this
        # May need some coref resolution, etc.
        domain_point_pattern = [
            [{"LOWER": "delay"}]
        ]
        dmatch = self.__matcher.match(domain_point_pattern, doc)

        if dmatch:
            result = 'delivery.delDueDate'
            return ScoredPrimitive(PointVDE(result), 1)

        if match:
            return ScoredPrimitive(PointVDE(match.text), 1)
        
        return None

