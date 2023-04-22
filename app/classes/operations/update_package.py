from app.classes.operations.contract_update_obj import ContractUpdateObj

# TODO: May try to more strongly type the new_value - alias of possibilities
class UpdatePackage:
    def __init__(self, update_obj: ContractUpdateObj = None, new_value: any = None):
        self.update_obj = update_obj
        self.new_value = new_value