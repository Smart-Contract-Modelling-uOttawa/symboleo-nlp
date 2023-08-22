from app.classes.units.unit_variety import UnitVariety
from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class AfterUnit(InputUnit):
    unit_type = UnitType.AFTER
    unit_var = UnitVariety.STATIC
    prompt = 'After'
    init_value = 'after'

class AtLeastUnit(InputUnit):
    unit_type = UnitType.AT_LEAST
    unit_var = UnitVariety.STATIC
    prompt = 'At least'
    init_value = 'at least'

class BeforeUnit(InputUnit):
    unit_type = UnitType.BEFORE
    unit_var = UnitVariety.STATIC
    prompt = 'Before'
    init_value = 'before'

class BetweenUnit(InputUnit):
    unit_type = UnitType.BETWEEN
    unit_var = UnitVariety.STATIC
    prompt = 'Between'
    init_value = 'between'

class ByUnit(InputUnit):
    unit_type = UnitType.BY
    unit_var = UnitVariety.STATIC
    prompt = 'By'
    init_value = 'by'

class DuringUnit(InputUnit):
    unit_type = UnitType.DURING
    unit_var = UnitVariety.STATIC
    prompt = 'During'
    init_value = 'during'

class FromUnit(InputUnit):
    unit_type = UnitType.FROM
    unit_var = UnitVariety.STATIC
    prompt = 'From'
    init_value = 'from'

class LaterThanUnit(InputUnit):
    unit_type = UnitType.LATER_THAN
    unit_var = UnitVariety.STATIC
    prompt = 'Later than'
    init_value = 'later than'

class PriorToUnit(InputUnit):
    unit_type = UnitType.PRIOR_TO
    unit_var = UnitVariety.STATIC
    prompt = 'Prior to'
    init_value = 'prior to'

class ThroughoutUnit(InputUnit):
    unit_type = UnitType.THROUGHOUT
    unit_var = UnitVariety.STATIC
    prompt = 'Throughout'
    init_value = 'throughout'

class UntilUnit(InputUnit):
    unit_type = UnitType.UNTIL
    unit_var = UnitVariety.STATIC
    prompt = 'Until'
    init_value = 'until'

class WithinUnit(InputUnit):
    unit_type = UnitType.WITHIN
    unit_var = UnitVariety.STATIC
    prompt = 'Within'
    init_value = 'within'