from app.classes.spec.norm import INorm
from app.classes.elements.element import Element
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage

# Currently not used.
class StandardEventNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: Element,  value: any) -> UpdatePackage:
        return UpdatePackage(new_value = value)
        

