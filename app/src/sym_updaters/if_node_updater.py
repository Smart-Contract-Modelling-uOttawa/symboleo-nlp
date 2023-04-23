import copy
from app.classes.spec.norm import INorm
from app.classes.selection.if_node import IfNode
from app.classes.spec.sym_event import SymEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.operations.contract_update_obj import ContractUpdateObj
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage

class IfNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: IfNode, value: any) -> UpdatePackage:
        if isinstance(value, SymEvent):
            predicate = PredicateFunctionHappens(value)
            new_norm = copy.deepcopy(norm)
            new_norm.update('trigger', predicate)
            update_obj = ContractUpdateObj(norms=[new_norm])

            return UpdatePackage(update_obj=update_obj)
