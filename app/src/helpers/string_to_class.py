import sys
from re import sub
from app.classes.spec import *
from app.classes.spec.p_atoms import *
from app.classes.spec.predicate_function import *
from app.classes.spec.sym_interval import *
from app.classes.spec.sym_point import *
from app.classes.spec.sym_event import *
from app.classes.spec.sym_situation import *


class StringToClass:
    @staticmethod
    def convert(classname: str):
        return getattr(sys.modules[__name__], classname)

class CaseConverter:
    @staticmethod
    def to_pascal(s: str):
        res = s.replace("_", " ").title().replace(" ", "")
        return res

    @staticmethod
    def to_snake(s: str):
        return '_'.join(
            sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
            s.replace('-', ' '))).split()).lower()
    