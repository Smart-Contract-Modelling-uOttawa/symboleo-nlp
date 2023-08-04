from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType, UnitVariety

class ObligationActionUnit(InputUnit):
    unit_type = UnitType.OBLIGATION_ACTION
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Obligation Action'
    needs_value = True

class ObligationSubjectUnit(InputUnit):
    unit_type = UnitType.OBLIGATION_SUBJECT
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Obligation Subject'
    needs_value = True


class ContractActionUnit(InputUnit):
    unit_type = UnitType.CONTRACT_ACTION
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Contract Action'
    needs_value = True

class ContractSubjectUnit(InputUnit):
    unit_type = UnitType.CONTRACT_SUBJECT
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Contract Subject'

class ContractEventUnit(InputUnit):
    unit_type = UnitType.CONTRACT_EVENT
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Contract Event'

class NormEventUnit(InputUnit):
    unit_type = UnitType.NORM_EVENT
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Norm Event'
    needs_value = True

