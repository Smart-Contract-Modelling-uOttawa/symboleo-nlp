from typing import Dict
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import AssetDeclaration, RoleDeclaration, EventDeclaration, DeclarationProp
from app.classes.spec.norm import Obligation, Power
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.contract_spec_parameter import ContractSpecParameter as Parm
from app.classes.spec.other_predicates import *

arg_values = {
     'client_id': 'client',
     'contractor_id': 'contractor',
     'subcontractor_id': 'subcontractor',
     'fee': 100,
     'invoice_payment': 'invoice',
     'pro_rata_payment': 'pro rata payment of the Compensation to the date of termination',
     'expenses_payment': 'reasonable and necessary expenses', 
     'subcontractor_payment': 'subcontractor services'

}

def get_contract_spec(arg_dict: Dict[str,str] = arg_values):

    parameters = [
        Parm('client_id', 'String'),
        Parm('contractor_id', 'String'),
        Parm('subcontractor_id', 'String'),
        Parm('fee', 'Number'),
        Parm('invoice_payment', 'String'),
        Parm('pro_rata_payment', 'String'),
        Parm('expenses_payment', 'String'),
        Parm('subcontractor_payment', 'String')
    ]

    # Declarations
    client = RoleDeclaration(arg_dict["client_id"], 'Client')
    contractor = RoleDeclaration(arg_dict["contractor_id"], 'Contractor')
    subcontractor = RoleDeclaration(arg_dict["subcontractor_id"], 'Subcontractor')
    
    CLIENT = client.to_obj()
    CONTRACTOR = contractor.to_obj()
    SUBCONTRACTOR = subcontractor.to_obj()
    
    services = AssetDeclaration('services', 'Services', [])
    SERVICES = services.to_obj()

    evt_invoice = EventDeclaration('evt_invoice', 'Invoice', [
        DeclarationProp('agent', CONTRACTOR, 'Role'),
        DeclarationProp('target', CLIENT, 'Role'),
    ])

    evt_pay_invoice = EventDeclaration('evt_pay_invoice', 'Pay', [
        DeclarationProp('from', CLIENT, 'Role'),
        DeclarationProp('to', CONTRACTOR, 'Role'),
        DeclarationProp('payment', f'"{arg_dict["contractor_id"]}"', 'String'),
    ])

    evt_pay_pro_rata = EventDeclaration('evt_pay_pro_rata', 'Pay', [
        DeclarationProp('from', CLIENT, 'Role'),
        DeclarationProp('to', CONTRACTOR, 'Role'),
        DeclarationProp('payment', f'"{arg_dict["contractor_id"]}"', 'String'),
    ])

    evt_reimburse_expenses = EventDeclaration('evt_reimburse_expenses', 'Pay', [
        DeclarationProp('from', CLIENT, 'Role'),
        DeclarationProp('to', CONTRACTOR, 'Role'),
        DeclarationProp('payment', f'"{arg_dict["expenses_payment"]}"', 'String'),
    ])

    evt_disclose_contractor = EventDeclaration('evt_disclose_contractor', 'Disclose', [
        DeclarationProp('agent', CONTRACTOR, 'Role')
    ])

    evt_hire_subcontractor = EventDeclaration('evt_hire_subcontractor', 'HireSubcontractor', [
        DeclarationProp('agent', CLIENT, 'Role'),
        DeclarationProp('subcontractor', SUBCONTRACTOR, 'Role')
    ]) 
    
    EVT_INVOICE = evt_invoice.to_obj()
    EVT_PAY_INVOICE = evt_pay_invoice.to_obj()
    EVT_PAY_PRO_RATA = evt_pay_pro_rata.to_obj()
    EVT_REIMBURSE_EXPENSES = evt_reimburse_expenses.to_obj()
    EVT_DISCLOSE_CONTRACTOR = evt_disclose_contractor.to_obj()
    EVT_HIRE_SUBCONTRACTOR = evt_hire_subcontractor.to_obj()

    # Declarations
    declarations = {
        'client': client,
        'contractor': contractor,
        'subcontractor': subcontractor,
        'services': services,
        'evt_invoice': evt_invoice,
        'evt_pay_invoice': evt_pay_invoice,
        'evt_pay_pro_rata': evt_pay_pro_rata,
        'evt_reimburse_expenses': evt_reimburse_expenses,
        'evt_disclose_contractor': evt_disclose_contractor,
        'evt_hire_subcontractor': evt_hire_subcontractor,
    }

  
    # Contract Spec
    contract_spec = ContractSpec(
        'IndependentContractor',
        parameters = parameters,
        declarations = declarations,
        obligations = {
            'ob_invoice': Obligation(
                'ob_invoice',
                None,
                # PropMaker.make(
                #     PredicateFunctionHappens(EVT_COMPLETE_SERVICES)
                # ),
                CONTRACTOR,
                CLIENT,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_INVOICE)
                )
            ),

            'ob_invoice_due': Obligation(
                'ob_invoice_due',
                None,
                CLIENT,
                CONTRACTOR,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_PAY_INVOICE)
                    # PredicateFunctionWHappensBefore(
                    #     EVT_PAY_INVOICE, 
                    #     PointFunction(
                    #         EVT_INVOICE,
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
                PropMaker.make_default(),
                # PropMaker.make_multiple([
                #     (PredicateFunctionHappens(EVT_START_SERVICES), False),
                #     (PredicateFunctionHappens(EVT_COMPLETE_SERVICES), True),
                #     (PredicateFunctionHappens(EVT_BREACH_CONTRACTOR), True)
                # ]),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_PAY_PRO_RATA)
                )
            ),

            'ob_reimburse': Obligation(
                'ob_reimburse',
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

            'ob_not_subcontract': Obligation(
                'ob_not_subcontract',
                None,
                CLIENT,
                CONTRACTOR,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_HIRE_SUBCONTRACTOR),
                    negation=True
                )
            ),
        },

        powers = {
            # 'pow_suspend_ob_not_disclose': Power(
            #     'pow_suspend_ob_not_disclose',
            #     PropMaker.make(
            #         PredicateFunctionHappens(
            #             EVT_AUTHORIZE_DISCLOSURE
            #         )
            #     ),
            #     CONTRACTOR,
            #     CLIENT,
            #     PropMaker.make_default(),
            #     PFObligation(PFObligationName.Suspended, 'ob_not_disclose')
            # )
        }
    )

    return contract_spec
