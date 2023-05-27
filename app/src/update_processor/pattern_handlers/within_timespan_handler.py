import copy
from app.classes.patterns.within_timespan_event import WithinTimespanEvent
from app.classes.spec.norm import Norm
from app.classes.spec.predicate_function import PredicateFunctionWHappensBefore
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.point_function import PointFunction
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.other.timespan import Timespan
from app.src.update_processor.pattern_handlers.pattern_handler import HandleObject, IHandlePatterns


class WithinTimespanHandler(IHandlePatterns):
    def handle(self, pattern: WithinTimespanEvent, handle_object: HandleObject):
        norm: Norm = handle_object.norm
        evt = pattern.event.to_sym_event()
        timespan = pattern.timespan

        init_event = norm.get_default_event('consequent') # Need to get consequent?
        point_func = Point(PointFunction(evt, timespan.time_value, timespan.time_unit))
        updated_predicate = PredicateFunctionWHappensBefore(init_event, point_func)
        new_norm = copy.deepcopy(norm)
        new_norm.update('consequent', updated_predicate)
        
        return [new_norm]