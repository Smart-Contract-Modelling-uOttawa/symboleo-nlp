from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType, UnitVariety

class ExceptUnit(InputUnit):
    unit_type = UnitType.EXCEPT
    unit_var = UnitVariety.STATIC
    prompt = 'Except'
    init_value = 'except'

class FailsToUnit(InputUnit):
    unit_type = UnitType.FAILS_TO
    unit_var = UnitVariety.STATIC
    prompt = 'Fails to'
    init_value = 'fails to'

class NotUnit(InputUnit):
    unit_type = UnitType.NOT
    unit_var = UnitVariety.STATIC
    prompt = 'Not'
    init_value = 'not'

class FinalUnit(InputUnit):
    unit_type = UnitType.FINAL_NODE
    unit_var = UnitVariety.EMPTY
    prompt = 'FINISH'
    init_value = ''

class ForUnit(InputUnit):
    unit_type = UnitType.FOR
    unit_var = UnitVariety.STATIC
    prompt = 'For'
    init_value = 'for'

class OfUnit(InputUnit):
    unit_type = UnitType.OF
    unit_var = UnitVariety.STATIC
    prompt = 'Of'
    init_value = 'of'

class RootUnit(InputUnit):
    unit_type = UnitType.ROOT
    unit_var = UnitVariety.EMPTY
    prompt = 'ROOT'

class UnlessUnit(InputUnit):
    unit_type = UnitType.UNLESS
    unit_var = UnitVariety.STATIC
    prompt = 'Unless'
    init_value = 'unless'

class WithUnit(InputUnit):
    unit_type = UnitType.WITH
    unit_var = UnitVariety.STATIC
    prompt = 'With'
    init_value = 'with'

class WithoutUnit(InputUnit):
    unit_type = UnitType.WITHOUT
    unit_var = UnitVariety.STATIC
    prompt = 'Without'
    init_value = 'without'
