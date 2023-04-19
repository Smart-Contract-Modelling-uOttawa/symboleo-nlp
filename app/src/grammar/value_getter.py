from app.classes.tokens.abstract_node import AbstractNode

class IGetValues:
    def get(self, node: AbstractNode) -> str:
        raise NotImplementedError()
    
class ValueGetter(IGetValues):
    def get(self, node: AbstractNode) -> str:
        if not node.needs_value:
            return node.init_value

        # present prompt
        # present options, if any
        user_input = input(f'{node.prompt}: ')

        # Can do some basic validation... or not

        return user_input