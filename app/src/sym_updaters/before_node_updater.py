import copy
from app.classes.spec.norm import INorm
from app.classes.selection.before_node import BeforeNode
from app.classes.spec.sym_event import SymEvent
from app.classes.spec.sym_point import SymPoint, PointExpression
from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent, PredicateFunctionWHappensBefore
from app.classes.operations.contract_update_obj import ContractUpdateObj
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage

class BeforeNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: BeforeNode, value: any) -> UpdatePackage:
        if isinstance(value, SymEvent):
            init_event = norm.get_default_event('consequent') # Need to get consequent?
            updated_predicate = PredicateFunctionWHappensBeforeEvent(init_event, value)
            new_norm = copy.deepcopy(norm)
            new_norm.update('consequent', updated_predicate)
            update_obj = ContractUpdateObj(norms=[new_norm])

            return UpdatePackage(update_obj=update_obj)
        
        if isinstance(value, PointExpression):
            init_event = norm.get_default_event('consequent') # Need to get consequent?
            updated_predicate = PredicateFunctionWHappensBefore(init_event, value)
            new_norm = copy.deepcopy(norm)
            new_norm.update('consequent', updated_predicate)
            update_obj = ContractUpdateObj(norms=[new_norm])

            return UpdatePackage(update_obj=update_obj)
