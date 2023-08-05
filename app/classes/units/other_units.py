from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType, UnitVariety

class ExceptUnit(InputUnit):
    unit_type = UnitType.EXCEPT
    unit_var = UnitVariety.STATIC
    prompt = 'Except'
    init_value = 'except'

# TODO: Am I supporting this?
class FailsToUnit(InputUnit):
    unit_type = UnitType.FAILS_TO
    unit_var = UnitVariety.STATIC
    prompt = 'fails to'
    init_value = 'fails to'

# TODO: Do I need this?
class FinalUnit(InputUnit):
    unit_type = UnitType.FINAL_NODE
    unit_var = UnitVariety.EMPTY
    prompt = 'FINISH'
    init_value = 'X'

class ForUnit(InputUnit):
    unit_type = UnitType.FOR
    unit_var = UnitVariety.STATIC
    prompt = 'For'
    init_value = 'for'

class NoticeEventUnit(InputUnit):
    unit_type = UnitType.NOTICE_EVENT
    unit_var = UnitVariety.EMPTY
    prompt = 'Notice Event'

class NoticeFromUnit(InputUnit):
    unit_type = UnitType.NOTICE_FROM
    unit_var = UnitVariety.STATIC
    prompt = 'Notice from'
    init_value = 'termination notice from'

class NotifierUnit(InputUnit):
    unit_type = UnitType.NOTIFIER
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Notifier'

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
