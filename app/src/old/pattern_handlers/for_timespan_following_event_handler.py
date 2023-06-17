import copy
from app.classes.patterns.for_timespan_following_event import ForTimespanFollowingEvent
from app.classes.spec.norm import Norm
from app.classes.spec.predicate_function import PredicateFunctionHappensWithin, PredicateFunctionWHappensBefore
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE, StartPoint
from app.classes.spec.point_function import PointFunction
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.elements.timespan import Timespan
from app.src.update_processor.pattern_handlers.pattern_handler import HandleObject, IHandlePatterns


class ForTimespanFollowingEventHandler(IHandlePatterns):
    def handle(self, pattern: ForTimespanFollowingEvent, handle_object: HandleObject):
        norm: Norm = handle_object.norm
        evt = pattern.event.to_sym_event()
        timespan = pattern.timespan

        init_event = norm.get_default_event('consequent') 
        point = Point(PointFunction(evt, timespan.time_value, timespan.time_unit))
        updated_predicate = PredicateFunctionWHappensBefore(init_event, point)
    
        new_norm = copy.deepcopy(norm)
        new_norm.update('consequent', updated_predicate)
        
        return [new_norm]