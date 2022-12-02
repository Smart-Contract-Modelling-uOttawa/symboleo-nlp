from app.src.matcher_helper import IGetMatches
from app.classes.spec.sym_point import PointVDE, PointFunction, PointAtomParameterDotExpression
from app.classes.spec.helpers import TimeUnitStr, TimeValueInt
from app.classes.spec.primitive import ScoredPrimitive
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives

class PointFunctionIdentifier(IIdentifyPrimitives):
    def __init__(
        self,
        matcher: IGetMatches
    ):
        self.__matcher = matcher

    def identify(self, doc) -> ScoredPrimitive:
        # This is where it would get recursive. 
        # I need it to look at the args for PointFunction
        # And then get each of those identifiers
        # And scoop them all up
        # This steals some o the work from the dynamic constructor, and myabe thats ok?
        
        # TODO: Make this all dynamic!
        time_value = TimeValueInt(10)
        time_unit = TimeUnitStr('days')
        point_atom = PointAtomParameterDotExpression(
            PointVDE('delivery.delDueDate')
        )

        prim = PointFunction(point_atom, time_value, time_unit)
        
        return ScoredPrimitive(prim, 1)

