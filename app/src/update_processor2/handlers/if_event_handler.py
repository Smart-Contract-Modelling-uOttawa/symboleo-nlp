import copy
from app.classes.patterns.pattern_classes import IfEvent
from app.classes.spec.norm import Norm
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.point_function import PointFunction
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.elements.timespan import Timespan
from app.src.update_processor.pattern_handlers.pattern_handler import HandleObject
from app.src.update_processor2.handlers.norm_update_handler import IHandleNormUpdates


class IfEventHandler(IHandleNormUpdates):
    def handle(self, pattern_class: IfEvent, handle_object: HandleObject):
        evt = pattern_class.event
        predicate = PredicateFunctionHappens(evt)
        new_norm = copy.deepcopy(handle_object.norm)
        new_norm.update('antecedent', predicate)

        return [new_norm]