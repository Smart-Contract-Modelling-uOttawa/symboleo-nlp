import copy
from app.classes.spec.norm import INorm
from app.classes.selection.selected_node import SelectedNode
from app.classes.spec.sym_event import SymEvent
from app.classes.other.contract_update_obj import UpdatePackage, ContractUpdateObj
from app.src.updaters.iupdate_package import IUpdatePackage

from app.src.operations.norm_builder import IBuildNorms

class UntilNodeUpdater(IUpdatePackage):
    def __init__(self, norm_builder: IBuildNorms):
        self.__norm_builder = norm_builder

    def update_package(self, norm: INorm, node: SelectedNode,  value: any) -> UpdatePackage:
        if isinstance(value, SymEvent):
            new_power = self.__norm_builder.build(norm, value)
            update_obj = ContractUpdateObj(norms=[new_power])
            return UpdatePackage(update_obj=update_obj)
        
        # if isinstance(value, PointExpression):
        #     init_event = norm.get_default_event('consequent') # Need to get consequent?
        #     updated_predicate = PredicateFunctionWHappensBefore(init_event, value)
        #     new_norm = copy.deepcopy(norm)
        #     new_norm.update('consequent', updated_predicate)
        #     update_obj = ContractUpdateObj(norms=[new_norm])

        #     return UpdatePackage(update_obj=update_obj)
