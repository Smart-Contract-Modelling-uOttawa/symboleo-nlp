import copy
from app.classes.frames.before_date_frame import BeforeDateFrame
from app.classes.spec.norm import Norm
from app.classes.spec.predicate_function import PredicateFunctionSHappensBefore
from app.classes.spec.sym_point import Point, PointVDE
from app.src.update_processor.pattern_handlers.handle_object import HandleObject
from app.src.update_processor.pattern_handlers.pattern_handler import IHandlePatterns


class BeforeDateHandler(IHandlePatterns):
    def handle(self, frame: BeforeDateFrame, handle_object: HandleObject):
        norm: Norm = handle_object.norm
        init_event = norm.get_default_event('consequent') # Need to get consequent?
        point_val = Point(PointVDE(frame.date_text))
        updated_predicate = PredicateFunctionSHappensBefore(init_event, point_val)
        new_norm = copy.deepcopy(norm)
        new_norm.update('consequent', updated_predicate)
        
        return [new_norm]