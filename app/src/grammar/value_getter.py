from app.classes.tokens.abstract_node import AbstractNode
from app.classes.other.user_input import UserInput

class IGetValues:
    def get(self, node: AbstractNode) -> UserInput:
        raise NotImplementedError()
    
class ValueGetter(IGetValues):
    def get(self, node: AbstractNode) -> str:
        if not node.needs_value:
            str_val = node.init_value
        else:
            # present prompt
            # present options, if any
            str_val = input(f'{node.prompt}: ')

            # Can do some basic validation... or not

        return UserInput(node.node_type, str_val)