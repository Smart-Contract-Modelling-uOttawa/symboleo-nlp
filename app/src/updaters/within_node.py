import copy
from app.classes.spec.norm import INorm
from app.classes.selection.selected_node import SelectedNode
from app.classes.spec.point_function import PointFunction
from app.classes.spec.predicate_function import PredicateFunctionWHappensBefore
from app.classes.other.contract_update_obj import UpdatePackage, ContractUpdateObj
from app.src.updaters.iupdate_package import IUpdatePackage

class WithinNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
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
