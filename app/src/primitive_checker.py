from app.classes.spec.primitive import Primitive
from app.src.string_to_class import StringToClass

class ICheckPrimitives:
    def check(self, name: str, primitives: list[Primitive]):
        raise NotImplementedError()
    

class PrimitiveChecker(ICheckPrimitives):
    def check(self, classname: str, primitives: list[Primitive]):
        target_class = StringToClass.convert(classname)

        # May need a priority function here if there are multiple...
        for x in primitives:
            if type(x) == target_class:
                return x
        return None
