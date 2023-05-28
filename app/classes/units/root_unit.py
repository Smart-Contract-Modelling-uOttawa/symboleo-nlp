from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.if_unit import IfUnit
from app.classes.units.before_unit import BeforeUnit
from app.classes.units.until_unit import UntilUnit
from app.classes.units.within_unit import WithinUnit
from app.classes.units.after_unit import AfterUnit

class RootUnit(InputUnit):
    unit_type = UnitType.ROOT
    children = [IfUnit, BeforeUnit, UntilUnit, WithinUnit, AfterUnit]
