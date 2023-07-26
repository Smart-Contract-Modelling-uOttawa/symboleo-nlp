from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class AfterUnit(InputUnit):
    unit_type = UnitType.AFTER
    prompt = 'after'
    init_value = 'after'

class BeforeUnit(InputUnit):
    unit_type = UnitType.BEFORE
    prompt = 'before'
    init_value = 'before'

class BetweenUnit(InputUnit):
    unit_type = UnitType.BETWEEN
    prompt = 'between'
    init_value = 'between'

class ByUnit(InputUnit):
    unit_type = UnitType.BY
    prompt = 'by'
    init_value = 'by'

class DuringUnit(InputUnit):
    unit_type = UnitType.DURING
    prompt = 'during'
    init_value = 'during'

class FromUnit(InputUnit):
    unit_type = UnitType.OF
    prompt = 'From'
    init_value = 'from'

class LaterThanUnit(InputUnit):
    unit_type = UnitType.LATER_THAN
    prompt = 'Later than'
    init_value = 'later than'

class PriorToUnit(InputUnit):
    unit_type = UnitType.PRIOR_TO
    prompt = 'Prior To'
    init_value = 'prior to'

class ThroughoutUnit(InputUnit):
    unit_type = UnitType.THROUGHOUT
    prompt = 'Throughout'
    init_value = 'throughout'

class UntilUnit(InputUnit):
    unit_type = UnitType.UNTIL
    prompt = 'Until'
    init_value = 'until'

class WithinUnit(InputUnit):
    unit_type = UnitType.WITHIN
    prompt = 'Within'
    init_value = 'within'