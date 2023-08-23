from tests.full_tests.isolated_test_cases.TestSymboleoContract import TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, Asset, DomainEvent, DomainProp
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import RoleDeclaration, AssetDeclaration, EventDeclaration, DeclarationProp
from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionWHappensBeforeEvent
from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig


# Distributor shall obtain an RMA number [P1]
## Original: prior to returning any product to Cisco
## CNL: Before Distributor returns any product to Cisco 
## BEFORE EVENT => WHappensBeforeEvent

test_case = TestCase(
    'before_event',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'Distributor': Role('Distributor', []),
                'Cisco': Role('Cisco', [])
            },
            assets = {},
            events = {'ObtainRmaNumber': DomainEvent('ObtainRmaNumber', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'distributor': RoleDeclaration('distributor', 'Distributor'),
                'cisco': RoleDeclaration('cisco', 'Cisco'),
                'evt_obtain_rma_number': EventDeclaration('evt_obtain_rma_number', 'ObtainRmaNumber')
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_obtain_rma_number': Obligation('ob_obtain_rma_number', None, 'distributor', 'cisco', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_obtain_rma_number')))
                )
            },
            surviving_obligations={},
            powers = {},
            constraints=[],
            parameters=[]
        ),
        NLTemplate(
            {   
                'nl_key': TemplateObj(
                    'Distributor shall obtain an RMA number [P1]', 
                    {'P1': [ParameterConfig('obligations', 'ob_obtain_rma_number', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.BEFORE, 'before'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'distributor'),
            UserInput(UnitType.TRANSITIVE_VERB, 'returns'),
            UserInput(UnitType.DOBJ, 'any product'),
            UserInput(UnitType.PREP_PHRASE, 'to cisco')
        ],
        nl_key='nl_key',
        parm_key='P1'
    ),
    
    exp_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'Distributor': Role('Distributor', []),
                'Cisco': Role('Cisco', [])
            },
            assets = {
                'Product': Asset('Product', []),
            },
            events = {
                'ObtainRmaNumber': DomainEvent('ObtainRmaNumber', []),
                'ReturnProduct': DomainEvent('ReturnProduct', [
                    DomainProp('returning_agent', 'Role'),
                    DomainProp('returned_object', 'Product'),
                    DomainProp('returning_target', 'Role'),
                ])
                },
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'distributor': RoleDeclaration('distributor', 'Distributor'),
                'cisco': RoleDeclaration('cisco', 'Cisco'),
                'product': AssetDeclaration('product', 'Product'),
                'evt_obtain_rma_number': EventDeclaration('evt_obtain_rma_number', 'ObtainRmaNumber'),
                'evt_return_product': EventDeclaration('evt_return_product', 'ReturnProduct', [
                    DeclarationProp('returning_agent', 'distributor', 'Role'),
                    DeclarationProp('returning_target', 'cisco', 'Role'),
                    DeclarationProp('returned_object', 'product', 'Product'),
                ]),
                'evt_obtain_rma_number': EventDeclaration('evt_obtain_rma_number', 'ObtainRmaNumber'),
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_obtain_rma_number': Obligation(
                    'ob_obtain_rma_number', 
                    None, 
                    'distributor', 
                    'cisco', 
                    PropMaker.make_default(), 
                    PropMaker.make(
                        PredicateFunctionWHappensBeforeEvent(
                            VariableEvent('evt_obtain_rma_number'), 
                            VariableEvent('evt_return_product')
                        )
                    )
                )
            },
            surviving_obligations={},
            powers = {},
            constraints=[],
            parameters=[]
        ),
        NLTemplate(
            {   
                'nl_key': TemplateObj(
                    'Distributor shall obtain an RMA number before distributor returns any product to cisco', 
                    {'P1': [ParameterConfig('obligations', 'ob_obtain_rma_number', 'consequent')]}
                )
            }
        )
    ),
)



