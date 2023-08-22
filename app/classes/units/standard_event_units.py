from app.classes.units.unit_variety import UnitVariety
from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class ContractActionUnit(InputUnit):
    unit_type = UnitType.CONTRACT_ACTION
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Contract Action'

class ContractSubjectUnit(InputUnit):
    unit_type = UnitType.CONTRACT_SUBJECT
    unit_var = UnitVariety.STATIC
    prompt = 'Contract Subject'
    init_value = 'contract'

class ContractEventUnit(InputUnit):
    unit_type = UnitType.CONTRACT_EVENT
    unit_var = UnitVariety.EMPTY
    prompt = 'Contract Event'

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