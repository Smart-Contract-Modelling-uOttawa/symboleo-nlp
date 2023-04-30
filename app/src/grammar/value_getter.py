from app.classes.tokens.abstract_node import AbstractNode
from app.classes.operations.user_input import UserInput

# May move this to user_scripts... its an I/O concern
class IGetValues:
    def get(self, node: AbstractNode) -> UserInput:
        raise NotImplementedError()

class ValueGetter(IGetValues):
    def get(self, node: AbstractNode) -> str:
        if not node.needs_value:
            str_val = node.init_value
        else:
            
            if node.options:
                print(f'\noptions for {node.node_type.value}')
                for x in node.options:
                    print(f'- {x}')
            

            str_val = input(f'{node.prompt}: ')


        return UserInput(node.node_type, str_val)