from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType
from app.classes.units.custom_event_units import SubjectUnit

class ObligationActionUnit(InputUnit):
    unit_type = UnitType.OBLIGATION_ACTION
    prompt = 'Obligation Action'
    needs_value = True

class ObligationSubjectUnit(InputUnit):
    unit_type = UnitType.OBLIGATION_SUBJECT
    prompt = 'Obligation Subject'
    needs_value = True
    children = [ObligationActionUnit]

class NormEventUnit(InputUnit):
    unit_type = UnitType.NORM_EVENT
    prompt = 'Norm Event'
    needs_value = True
    children = [ObligationSubjectUnit]


class ContractActionUnit(InputUnit):
    unit_type = UnitType.CONTRACT_ACTION
    prompt = 'Contract Action'
    needs_value = True

class ContractSubjectUnit(InputUnit):
    unit_type = UnitType.CONTRACT_SUBJECT
    prompt = 'Contract Subject'
    children = [ContractActionUnit]

class ContractEventUnit(InputUnit):
    unit_type = UnitType.CONTRACT_EVENT
    prompt = 'Contract Event'
    children = [ContractSubjectUnit]

class CommonEventUnit(InputUnit):
    unit_type = UnitType.COMMON_EVENT
    prompt = 'Common Event'
    needs_value = True
    children = [SubjectUnit]

class StandardEventUnit(InputUnit):
    unit_type = UnitType.STANDARD_EVENT
    prompt = 'Standard Contract Event'
    children = [ContractEventUnit, NormEventUnit, CommonEventUnit]

