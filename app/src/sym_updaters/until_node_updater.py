import copy
from app.classes.spec.norm import INorm
from app.classes.elements.element import Element
from app.classes.spec.sym_event import SymEvent
from app.classes.operations.update_package import UpdatePackage
from app.classes.operations.contract_update_obj import ContractUpdateObj
from app.src.sym_updaters.package_updater import IUpdatePackage
from app.classes.spec.point_function import PointFunction
from app.classes.spec.predicate_function import PredicateFunctionWHappensBefore

from app.src.operations.norm_builder import IBuildNorms

class UntilNodeUpdater(IUpdatePackage):
    def __init__(self, norm_builder: IBuildNorms):
        self.__norm_builder = norm_builder

    def update_package(self, norm: INorm, node: Element, value: any) -> UpdatePackage:
        if isinstance(value, SymEvent):
            new_power = self.__norm_builder.build(norm, value)
            update_obj = ContractUpdateObj(norms=[new_power])
            return UpdatePackage(update_obj=update_obj)
        
        # dict - timespan + event ... may type this stronger (TODO)
        if isinstance(value, dict):
            time_unit = value['time_unit']
            time_value = value['time_value']
            event2 = value['event']

            init_event = norm.get_default_event('consequent')
            point_function = PointFunction(event2, time_value, time_unit)
            updated_predicate =  PredicateFunctionWHappensBefore(init_event, point_function)
            
            new_norm = copy.deepcopy(norm)
            new_norm.update('consequent', updated_predicate)
            update_obj = ContractUpdateObj(norms=[new_norm])

            return UpdatePackage(update_obj)
            