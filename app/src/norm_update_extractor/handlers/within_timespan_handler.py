import copy
from app.classes.patterns.pattern_classes import WithinTimespanEvent
from app.classes.spec.norm import Norm
from app.classes.spec.predicate_function import PredicateFunctionWHappensBefore
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.point_function import PointFunction
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.elements.timespan import Timespan
from app.classes.operations.handle_object import HandleObject
from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates


class WithinTimespanHandler(IHandleNormUpdates):
    def handle(self, pattern_class: WithinTimespanEvent, handle_object: HandleObject):
        norm: Norm = handle_object.norm
        evt = pattern_class.event
        init_event = norm.get_default_event('consequent') # Need to get consequent?
        point_func = Point(PointFunction(evt, pattern_class.timespan_value, pattern_class.timespan_unit))
        updated_predicate = PredicateFunctionWHappensBefore(init_event, point_func)
        new_norm = copy.deepcopy(norm)
        new_norm.update('consequent', updated_predicate)
        
        return [new_norm]