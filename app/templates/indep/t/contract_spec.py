from typing import Dict
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import AssetDeclaration, RoleDeclaration, EventDeclaration, DeclarationProp
from app.classes.spec.norm import Obligation, Power
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.sym_event import ContractEvent, ContractEventName
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.contract_spec_parameter import ContractSpecParameter as Parm
from app.classes.spec.other_predicates import *

arg_values = {
     'client_name': 'client',
     'contractor_name': 'contractor'
}

def get_contract_spec(arg_dict: Dict[str,str] = arg_values):

    parameters = [
        Parm('client_name', 'String'),
        Parm('contractor_name', 'String')
    ]
    # 

    # Declarations
    client = RoleDeclaration(arg_dict["client_name"], 'Client')
    contractor = RoleDeclaration(arg_dict["contractor_name"], 'Contractor')
    CLIENT = client.to_obj()
    CONTRACTOR = contractor.to_obj()
    
    services = AssetDeclaration('services', 'Services', [])
    invoice = AssetDeclaration('invoice', 'Invoice', [])
    expenses = AssetDeclaration('expenses', 'Expenses', [])
    SERVICES = services.to_obj()
    INVOICE = invoice.to_obj()
    EXPENSES = expenses.to_obj()

    evt_start_services = EventDeclaration('evt_start_services', 'StartServices', [
        DeclarationProp('agent', CONTRACTOR, 'Role'),
        DeclarationProp('services', SERVICES, 'Services'),
    ])

    evt_complete_services = EventDeclaration('evt_complete_services', 'CompleteServices', [
        DeclarationProp('completing_agent', CONTRACTOR, 'Role'),
        DeclarationProp('completed_object', SERVICES, 'Services'),
    ])

    evt_send_invoice = EventDeclaration('evt_send_invoice', 'SendInvoice', [
        DeclarationProp('sending_agent', CONTRACTOR, 'Role'),
        DeclarationProp('sent_object', INVOICE, 'Invoice')
    ])

    evt_pay_invoice = EventDeclaration('evt_pay_invoice', 'PayInvoice', [
        DeclarationProp('from', CLIENT, 'Role'),
        DeclarationProp('to', CONTRACTOR, 'Role'),
        DeclarationProp('invoice', INVOICE, 'Invoice')
    ])

    evt_pay_pro_rata = EventDeclaration('evt_pay_pro_rata', 'PayProRata', [
        DeclarationProp('from', CLIENT, 'Role'),
        DeclarationProp('to', CONTRACTOR, 'Role')
    ])

    # evt_breach_contractor =  EventDeclaration('evt_breach_contractor', 'BreachContract', [
    #     DeclarationProp('agent', CONTRACTOR, 'Role')
    # ])

    evt_reimburse_expenses = EventDeclaration('evt_reimburse_expenses', 'ReimburseExpenses', [
        DeclarationProp('from', CLIENT, 'Role'),
        DeclarationProp('to', CONTRACTOR, 'Role'),
        DeclarationProp('expenses', EXPENSES, 'Expenses'),
    ])

    evt_disclose_contractor = EventDeclaration('evt_disclose_contractor', 'Disclose', [
        DeclarationProp('agent', CONTRACTOR, 'Role')
    ])

    # evt_authorize_disclosure = EventDeclaration('evt_authorize_disclosure', 'AuthorizeDisclosure', [
    #     DeclarationProp('agent', CLIENT, 'Role')
    # ])

    EVT_START_SERVICES = evt_start_services.to_obj()
    EVT_COMPLETE_SERVICES = evt_complete_services.to_obj()
    EVT_SEND_INVOICE = evt_send_invoice.to_obj()
    EVT_PAY_INVOICE = evt_pay_invoice.to_obj()
    EVT_PAY_PRO_RATA = evt_pay_pro_rata.to_obj()
    # EVT_BREACH_CONTRACTOR = evt_breach_contractor.to_obj()
    EVT_REIMBURSE_EXPENSES = evt_reimburse_expenses.to_obj()
    EVT_DISCLOSE_CONTRACTOR = evt_disclose_contractor.to_obj()
    # EVT_AUTHORIZE_DISCLOSURE = evt_authorize_disclosure.to_obj()

    # Declarations
    declarations = {
        'client': client,
        'contractor': contractor,
        
        'services': services,
        'invoice': invoice,
        'expenses': expenses,
        
        'evt_start_services': evt_start_services,
        'evt_complete_services': evt_complete_services,
        'evt_send_invoice': evt_send_invoice,
        'evt_pay_invoice': evt_pay_invoice,
        'evt_pay_pro_rata': evt_pay_pro_rata,
        # 'evt_breach_contractor': evt_breach_contractor,
        'evt_reimburse_expenses': evt_reimburse_expenses,
        'evt_disclose_contractor': evt_disclose_contractor,
        # 'evt_authorize_disclosure': evt_authorize_disclosure
    }

  
    # Contract Spec
    contract_spec = ContractSpec(
        'IndependentContractor',
        parameters = parameters,
        declarations = declarations,
        obligations = {
            'ob_send_invoice': Obligation(
                'ob_send_invoice',
                None,
                # PropMaker.make(
                #     PredicateFunctionHappens(EVT_COMPLETE_SERVICES)
                # ),
                CONTRACTOR,
                CLIENT,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_SEND_INVOICE)
                )
            ),

            'ob_pay_invoice': Obligation(
                'ob_pay_invoice',
                None,
                CLIENT,
                CONTRACTOR,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_PAY_INVOICE)
                    # PredicateFunctionWHappensBefore(
                    #     EVT_PAY_INVOICE, 
                    #     PointFunction(
                    #         EVT_SEND_INVOICE,
                    #         10,
                    #         TimeUnit.Days
                    #     )
                    # )
                )
            ),

            'ob_partial_completion': Obligation(
                'ob_partial_completion',
                None,
                CLIENT,
                CONTRACTOR,
                PropMaker.make_multiple([
                    (PredicateFunctionHappens(EVT_START_SERVICES), False),
                    (PredicateFunctionWHappensBeforeEvent(ContractEvent(ContractEventName.Terminated), EVT_COMPLETE_SERVICES), False),
                    # (PredicateFunctionHappens(EVT_BREACH_CONTRACTOR), True)
                ]),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_PAY_PRO_RATA)
                )
            ),

            'ob_reimburse_expenses': Obligation(
                'ob_reimburse_expenses',
                None,
                CLIENT,
                CONTRACTOR,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_REIMBURSE_EXPENSES)
                )
            ),

            'ob_not_disclose': Obligation(
                'ob_not_disclose',
                None,
                CONTRACTOR,
                CLIENT,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_DISCLOSE_CONTRACTOR),
                    negation=True
                )
            ),

        },

        powers = {
            'pow_terminate_ob_not_disclose': Power(
                'pow_terminate_ob_not_disclose',
                None,
                # PropMaker.make(
                #     PredicateFunctionHappens(
                #         EVT_AUTHORIZE_DISCLOSURE
                #     )
                # ),
                CONTRACTOR,
                CLIENT,
                PropMaker.make_default(),
                PFObligation(PFObligationName.Terminated, 'ob_not_disclose')
            )
        }
    )

    return contract_spec
