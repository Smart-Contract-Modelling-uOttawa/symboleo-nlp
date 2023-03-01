import sys
from app.classes.spec import *
from app.classes.spec.p_atoms import *
from app.classes.spec.predicate_function import *
from app.classes.spec.sym_interval import *
from app.classes.spec.sym_point import *
from app.classes.spec.sym_event import *
from app.classes.spec.sym_situation import *
from app.classes.spec.helpers import *

class StringToClass:
    @staticmethod
    def convert(classname: str):
        return getattr(sys.modules[__name__], classname)