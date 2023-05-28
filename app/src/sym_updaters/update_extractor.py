from typing import List, Dict, Type
from app.classes.spec.norm import INorm
from app.classes.elements.element import Element

from app.classes.operations.contract_update_obj import ContractUpdateObj
from app.src.sym_updaters.package_updater import IUpdatePackage

class IExtractUpdates:
    def extract(self, norm: INorm, nodes: List[Element]) -> ContractUpdateObj:
        raise NotImplementedError()


class UpdateExtractor(IExtractUpdates):
    def __init__(
        self, 
        updater_dict: Dict[Type[Element], IUpdatePackage]
    ):
        self.__updater_dict = updater_dict


    def extract(self, norm: INorm, nodes: List[Element]) -> ContractUpdateObj:
        update_obj = ContractUpdateObj()
        value = None

        for node in reversed(nodes):
            updater = self.__updater_dict[type(node)]
            package = updater.update_package(norm, node, value)
            update_obj.merge(package.update_obj)
            value = package.new_value
            
        return update_obj

