from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class ExceptUnit(InputUnit):
    unit_type = UnitType.EXCEPT
    prompt = 'Except'
    init_value = 'except'

# TODO: Am I supporting this?
class FailsToUnit(InputUnit):
    unit_type = UnitType.FAILS_TO
    prompt = 'fails to'
    init_value = 'fails to'

# TODO: Do I need this?
class FinalUnit(InputUnit):
    unit_type = UnitType.FINAL_NODE
    prompt = 'FINISH'
    needs_value = False
    init_value = 'X'

class ForUnit(InputUnit):
    unit_type = UnitType.FOR
    prompt = 'For'
    init_value = 'for'

class OfUnit(InputUnit):
    unit_type = UnitType.OF
    prompt = 'Of'
    init_value = 'of'

class RootUnit(InputUnit):
    unit_type = UnitType.ROOT

class UnlessUnit(InputUnit):
    unit_type = UnitType.UNLESS
    prompt = 'Unless'
    init_value = 'unless'

class WithUnit(InputUnit):
    unit_type = UnitType.WITH
    prompt = 'With'
    init_value = 'with'

class WithoutUnit(InputUnit):
    unit_type = UnitType.WITHOUT
    prompt = 'Without'
    init_value = 'without'