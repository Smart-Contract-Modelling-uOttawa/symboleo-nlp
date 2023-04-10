import copy
from app.classes.symboleo_contract import SymboleoContract, ContractSpec, DomainModel
from app.classes.spec.contract_spec import Norm, Obligation, Power
from app.classes.spec.prop_maker import PropMaker
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.sym_event import VariableEvent, ObligationEvent, ObligationEventName, ContractEvent, ContractEventName
from app.classes.spec.sym_point import PointVDE, PointAtomContractEvent
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.sym_situation import ObligationState, ObligationStateName
from app.classes.spec.contract_spec_other import ContractSpecParameter
from app.classes.spec.other_function import *
from app.src.helpers.declarer import Declarer

from app.templates.prop_mgmt.t_raw.domain_model import get_domain_model

def get_contract_spec():
    dm = get_domain_model()

    OWNER = 'owner'
    MANAGER = 'manager'
    PROPERTY = 'the_property'

    parameters = [
        ContractSpecParameter('manager', 'Manager'),
        ContractSpecParameter('owner', 'Owner'),
        ContractSpecParameter('var_ad_expenses', 'String'), # all expenses related to Advertising
        ContractSpecParameter('var_rent_proceeds', 'String'), # rent proceeds
        ContractSpecParameter('var_accounting_artifacts', 'String'), # rents, expenses, and disbursements
        ContractSpecParameter('var_repair_costs', 'String'), # the cost of all maintenance and repairs
        #ContractSpecParameter('var_days_notice', 'String'), # X
        ContractSpecParameter('var_termination_disbursement', 'String'), # any monies in the Manager\'s possession due
        ContractSpecParameter('var_termination_reimbursement', 'String'), #any expenses incurred or approved prior to the date of termination
    ]

    # Creating the objects
    the_property = Declarer.declare(dm, 'assets', 'Property', 'the_property', [
    ])
    evt_advertise = Declarer.declare(dm, 'events', 'Advertise', 'evt_advertise', [
        ('agent', MANAGER),
        ('property', PROPERTY)
    ])
    evt_reimburse_advertising = Declarer.declare(dm, 'events', 'Reimburse', 'evt_reimburse_advertisting', [
        ('from', OWNER),
        ('to', MANAGER),
        ('amount', 'var_ad_expenses')
    ])
    evt_notify_expenses = Declarer.declare(dm, 'events', 'Notify', 'evt_notify_expenses', [
        ('agent', MANAGER),
        ('target', OWNER),
        ('message', 'var_ad_expenses')
    ])
    evt_collect_rent = Declarer.declare(dm, 'events', 'CollectRent', 'evt_collect_rent', [
        ('agent', MANAGER),
        ('property', PROPERTY)
    ])
    evt_disburse = Declarer.declare(dm, 'events', 'Disburse', 'evt_disburse', [
        ('from', MANAGER),
        ('to', OWNER),
        ('amount', 'var_rent_proceeds')
    ])
    evt_accounting = Declarer.declare(dm, 'events', 'Accounting', 'evt_accounting', [
        ('agent', MANAGER),
        ('target', OWNER),
        ('object', 'var_accounting_artifacts')
    ])
    evt_repair = Declarer.declare(dm, 'events', 'Repair', 'evt_repair', [
        ('agent', MANAGER),
        ('property', PROPERTY)
    ])
    evt_reimburse_maintenance = Declarer.declare(dm, 'events', 'Reimburse', 'evt_reimburse_maintenance', [
        ('from', OWNER),
        ('to', MANAGER),
        ('amount', 'var_repair_costs')
    ])
    evt_repair_invoice = Declarer.declare(dm, 'events', 'ProvideInvoice', 'evt_repair_invoice', [
        ('agent', MANAGER),
        ('target', OWNER),
        ('object', 'var_repair_costs')
    ])
    # evt_legal_proceedings = Declarer.declare(dm, 'events', 'LegalProceedingsNecessary', 'evt_legal_proceedings', [
    #     ('property', PROPERTY)
    # ])
    evt_handle_legal = Declarer.declare(dm, 'events', 'HandleLegalProceedings', 'evt_handle_legal', [
        ('agent', MANAGER),
        ('property', PROPERTY)
    ])
    # evt_provide_termination_notice_owner = Declarer.declare(dm, 'events', 'ProvideTerminationNotice', 'evt_provide_termination_notice_owner', [
    #     ('agent', OWNER),
    #     ('target', MANAGER),
    #     ('numDays', 'var_days_notice')
    # ])
    # evt_provide_termination_notice_manager = Declarer.declare(dm, 'events', 'ProvideTerminationNotice', 'evt_provide_termination_notice_manager', [
    #     ('agent', MANAGER),
    #     ('target', OWNER),
    #     ('numDays', 'var_days_notice')
    # ])
    evt_disburse_termination = Declarer.declare(dm, 'events', 'Disburse', 'evt_disburse_termination', [
        ('from', MANAGER),
        ('to', OWNER),
        ('amount', 'var_termination_deisbursement')
    ])
    evt_reimburse_termination = Declarer.declare(dm, 'events', 'Reimburse', 'evt_reimburse_termination', [
        ('from', OWNER),
        ('to', MANAGER),
        ('amount', 'var_termination_reimbursement')
    ])

    # Declarations
    declarations = {
        'the_property': the_property,
        'evt_advertise': evt_advertise,
        'evt_reimburse_advertising': evt_reimburse_advertising,
        'evt_notify_expenses': evt_notify_expenses,
        'evt_collect_rent': evt_collect_rent,
        'evt_disburse': evt_disburse,
        'evt_accounting': evt_accounting,
        'evt_repair': evt_repair,
        'evt_reimburse_maintenance': evt_reimburse_maintenance,
        'evt_repair_invoice': evt_repair_invoice,
        # 'evt_legal_proceedings': evt_legal_proceedings,
        'evt_handle_legal': evt_handle_legal,
        # 'evt_provide_termination_notice_owner': evt_provide_termination_notice_owner,
        # 'evt_provide_termination_notice_manager': evt_provide_termination_notice_manager,
        'evt_disburse_termination': evt_disburse_termination,
        'evt_reimburse_termination': evt_reimburse_termination
    }

    # Variables to use
    THE_PROPERTY = the_property.to_obj()
    EVT_ADVERTISE = evt_advertise.to_obj()
    EVT_REIMBURSE_ADVERTISING = evt_reimburse_advertising.to_obj()
    EVT_NOTIFY_EXPENSES = evt_notify_expenses.to_obj()
    EVT_COLLECT_RENT = evt_collect_rent.to_obj()
    EVT_DISBURSE = evt_disburse.to_obj()
    EVT_ACCOUNTING = evt_accounting.to_obj()
    EVT_REPAIR = evt_repair.to_obj()
    EVT_REIMBURSE_MAINTENANCE = evt_reimburse_maintenance.to_obj()
    EVT_REPAIR_INVOICE = evt_repair_invoice.to_obj()
    # EVT_LEGAL_PROCEEDINGS = evt_legal_proceedings.to_obj()
    EVT_HANDLE_LEGAL = evt_handle_legal.to_obj()
    # EVT_PROVIDE_TERMINATION_NOTICE_OWNER = evt_provide_termination_notice_owner.to_obj()
    # EVT_PROVIDE_TERMINATION_NOTICE_MANAGER = evt_provide_termination_notice_manager.to_obj()
    EVT_DISBURSE_TERMINATION = evt_disburse_termination.to_obj()
    EVT_REIMBURSE_TERMINATION = evt_reimburse_termination.to_obj()    

    # Contract Spec
    contract_spec = ContractSpec(
        'PropMgmt',
        parameters = parameters,
        declarations = declarations,
        preconditions = [
            
        ],
        postconditions = [
            
        ],
        obligations = {
            'ob_advertise': Obligation(
                'ob_advertise',
                None,
                MANAGER,
                OWNER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_ADVERTISE)
                )
            ),
            'ob_reimburse': Obligation(
                'ob_reimburse',
                None,
                OWNER,
                MANAGER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_REIMBURSE_ADVERTISING)
                )
            ),
            'ob_notify_expense': Obligation(
                'ob_notify_expense',
                None,
                MANAGER,
                OWNER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_NOTIFY_EXPENSES)
                )
            ),
            'ob_collect_rent': Obligation(
                'ob_collect_rent',
                None,
                MANAGER,
                OWNER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_COLLECT_RENT)
                )
            ),
            'ob_disbursement': Obligation(
                'ob_disbursement',
                None,
                MANAGER,
                OWNER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_DISBURSE)
                )
            ),
            'ob_accounting': Obligation(
                'ob_accounting',
                None,
                MANAGER,
                OWNER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_ACCOUNTING)
                )
            ),
            'ob_repair': Obligation(
                'ob_repair',
                None,
                MANAGER,
                OWNER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_REPAIR)
                )
            ),
            'ob_reimburse_maintenance': Obligation(
                'ob_reimburse_maintenance',
                None,
                OWNER,
                MANAGER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_REIMBURSE_MAINTENANCE)
                )
            ),
            'ob_repair_invoice': Obligation(
                'ob_repair_invoice',
                None,
                MANAGER,
                OWNER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_REPAIR_INVOICE)
                )
            ),
            ## TODO: Use case for coreference ("such" legal proceeding...)
            ## Since there is a coreference, maybe shouldn't remove it?
            'ob_legal_proceedings': Obligation(
                'ob_legal_proceedings',
                None,
                # PropMaker.make(
                #     PredicateFunctionHappens(EVT_LEGAL_PROCEEDINGS)
                # ),
                MANAGER,
                OWNER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_HANDLE_LEGAL)
                )
            ),
            # TODO: Should we also remove the trigger here??? How do we handle TWO refinements...
            'ob_disburse_termination': Obligation(
                'ob_disburse_termination',
                None,
                # PropMaker.make(
                #     PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))
                # ),
                MANAGER,
                OWNER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_DISBURSE_TERMINATION)
                    # PredicateFunctionSHappensBefore(
                    #     EVT_DISBURSE_TERMINATION, 
                    #     PointFunction(
                    #         PointAtomContractEvent(ContractEvent(ContractEventName.Terminated)),
                    #         3,
                    #         TimeUnit.Days
                    #     ))
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
                    # PredicateFunctionSHappensBefore(
                    #     EVT_REIMBURSE_TERMINATION, 
                    #     PointFunction(
                    #         PointAtomContractEvent(ContractEvent(ContractEventName.Terminated)),
                    #         10,
                    #         TimeUnit.Days
                    #     ))
                )
            ),

        },

        surviving_obligations = {
           
        },
        powers = {
            # 'pow_terminate_notice_owner': Power(
            #     'pow_terminate_notice_owner',
            #     PropMaker.make(
            #         PredicateFunctionHappens(
            #             EVT_PROVIDE_TERMINATION_NOTICE_OWNER
            #         )
            #     ),
            #     OWNER,
            #     MANAGER,
            #     PropMaker.make_default(),
            #     PFContract(PFContractName.Terminated)
            # ),
            # 'pow_terminate_notice_manager': Power(
            #     'pow_terminate_notice_manager',
            #     PropMaker.make(
            #         PredicateFunctionHappens(
            #             EVT_PROVIDE_TERMINATION_NOTICE_MANAGER
            #         )
            #     ),
            #     MANAGER,
            #     OWNER,
            #     PropMaker.make_default(),
            #     PFContract(PFContractName.Terminated)
            # )
        },
        constraints = [
        ]
    )

    return contract_spec
