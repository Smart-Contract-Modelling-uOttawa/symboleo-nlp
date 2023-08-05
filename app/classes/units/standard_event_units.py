from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType, UnitVariety

class ObligationActionUnit(InputUnit):
    unit_type = UnitType.OBLIGATION_ACTION
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Obligation Action'

class ObligationSubjectUnit(InputUnit):
    unit_type = UnitType.OBLIGATION_SUBJECT
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Obligation Subject'

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

class NormEventUnit(InputUnit):
    unit_type = UnitType.NORM_EVENT
    unit_var = UnitVariety.EMPTY
    prompt = 'Norm Event'

