from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.elements.element import Element
from app.classes.units.input_unit import InputUnit

from app.src.grammar.token_processor import IProcessToken

from app.src.grammar.value_getter import IGetValues
from app.src.grammar.input_converter import IConvertInput

class SimpleTokenProcessor(IProcessToken):
    def __init__(
        self,
        value_getter: IGetValues,
        input_converter: IConvertInput
    ):
        self.__value_getter = value_getter
        self.__input_converter = input_converter


    def process(self, token: InputUnit, contract: ISymboleoContract) -> Element:
        user_input = self.__value_getter.get(token) # pass in contract...
        result = self.__input_converter.convert([user_input])[0]
        return result
