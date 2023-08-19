from typing import Dict
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import AssetDeclaration, RoleDeclaration, EventDeclaration, DeclarationProp
from app.classes.spec.norm import Obligation, Power
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.sym_event import ContractEvent, ContractEventName
from app.classes.spec.sym_point import PointVDE, PointAtomContractEvent
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.contract_spec_parameter import ContractSpecParameter as Parm
from app.classes.spec.other_predicates import *

arg_values = {
     'manager_id': 'manager',
     'owner_id': 'owner',
     'property_address': '123 Main Street',
     'var_termination_disbursement': 'any monies in the Manager\'s possession due',
     'var_termination_reimbursement': 'any expenses incurred or approved prior to the date of termination'
}

def get_contract_spec(arg_dict: Dict[str,str] = arg_values):

    parameters = [
        Parm('manager_id', 'String'),
        Parm('owner_id', 'String'),
        Parm('property_address', 'String'),
        Parm('var_termination_disbursement', 'String'), 
        Parm('var_termination_reimbursement', 'String'),
    ]

    # Declarations
    manager = RoleDeclaration(arg_dict["manager_id"], 'Manager')
    owner = RoleDeclaration(arg_dict["owner_id"], 'Owner')
    MANAGER = manager.to_obj()
    OWNER = owner.to_obj()
    
    the_property = AssetDeclaration('property', 'RentalProperty', [
        DeclarationProp('address', f'"{arg_dict["property_address"]}"','String')
    ])
    legal_proceedings = AssetDeclaration('legal proceedings', 'LegalProceedings', id = 'legal_proceedings')
    PROPERTY = the_property.to_obj()
    LEGAL_PROCEEDINGS = legal_proceedings.to_obj()

    evt_handle_legal_proceedings = EventDeclaration('evt_handle_legal_proceedings', 'HandleLegalProceedings', [
        DeclarationProp('agent', MANAGER, 'Role'),
        DeclarationProp('handled_object', LEGAL_PROCEEDINGS, 'LegalProceedings'),
    ])

    evt_disburse_termination = EventDeclaration('evt_disburse_termination', 'Disburse', [
        DeclarationProp('from', MANAGER, 'Role'),
        DeclarationProp('to', OWNER, 'Role'),
        DeclarationProp('amount', f'"{arg_dict["var_termination_disbursement"]}"', 'String'),
    ])

    evt_reimburse_termination = EventDeclaration('evt_reimburse_termination', 'Reimburse', [
        DeclarationProp('from', OWNER, 'Role'),
        DeclarationProp('to', MANAGER, 'Role'),
        DeclarationProp('amount', f'"{arg_dict["var_termination_reimbursement"]}"', 'String'),
    ])

    EVT_HANDLE_LEGAL_PROCEEDINGS = evt_handle_legal_proceedings.to_obj()
    EVT_DISBURSE_TERMINATION = evt_disburse_termination.to_obj()
    EVT_REIMBURSE_TERMINATION = evt_reimburse_termination.to_obj()  


    # Declarations
    declarations = {
        'manager': manager,
        'owner': owner,
        'property': the_property,
        'legal_proceedings': legal_proceedings,
        'evt_handle_legal_proceedings': evt_handle_legal_proceedings,
        'evt_disburse_termination': evt_disburse_termination,
        'evt_reimburse_termination': evt_reimburse_termination
    }

  
    # Contract Spec
    contract_spec = ContractSpec(
        'PropMgmt',
        parameters = parameters,
        declarations = declarations,
        obligations = {
            'ob_legal_proceedings': Obligation(
                'ob_legal_proceedings',
                None,
                MANAGER,
                OWNER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_HANDLE_LEGAL_PROCEEDINGS)
                )
            ),

            'ob_disburse_termination': Obligation(
                'ob_disburse_termination',
                None,
                MANAGER,
                OWNER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_DISBURSE_TERMINATION)
                )
            ),
            'ob_reimburse_termination': Obligation(
                'ob_reimburse_termination',
                None,
                OWNER,
                MANAGER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_REIMBURSE_TERMINATION)
                )
            ),

        },

        powers = {
        }
    )

    return contract_spec
