from app.classes.spec.norm import INorm
from app.classes.elements.element import Element
from app.classes.operations.update_package import UpdatePackage

class IUpdatePackage:
    def update_package(self, norm: INorm, node: Element,  value: any) -> UpdatePackage:
        raise NotImplementedError()


class DefaultUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: Element, value: any) -> UpdatePackage:
        return UpdatePackage(new_value = value)