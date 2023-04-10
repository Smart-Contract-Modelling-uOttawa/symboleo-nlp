from typing import Dict, List
from app.src.operations.parm_configs import ParameterConfig, ParameterSpec, ParmOpCode
from app.classes.nl_template import NLTemplate, TemplateObj

nl_template = NLTemplate(
    template_dict = {
        # Could break this up...
        'advertise': TemplateObj(
            'The Manager shall advertise the Property for rent, engage and screen potential renters, enter into rental agreement(s) with acceptable renter(s).',
            ['obligations.ob_advertise']
        ),
        'reimburse': TemplateObj(
            'The Owner shall reimburse the Manager for all expenses related to such Advertising. ',
            ['obligations.ob_reimburse']
        ),
        # TODO: "in advance" denotes something temporal...
        'notify_expense': TemplateObj(
            'The Manager shall notify the Owner, in advance, of anticipated expenses related to such Advertising.',
            ['obligations.ob_notify_expense']
        ),
        'collect_rent': TemplateObj(
            'The Manager shall be responsible for all collection of Rent earned on the Property.',
            ['obligations.ob_collect_rent']
        ),
        'disbursement': TemplateObj(
            'The Manager shall then be responsible for disbursement of those proceeds to the Owner.',
            ['obligations.ob_disbursement']
        ),
        'accounting': TemplateObj(
            'The Manager shall further prepare and provide to the Owner a detailed accounting of all rents, expenses, and disbursements.',
            ['obligations.ob_accounting']
        ),
        'repair': TemplateObj(
            'The Manager shall be responsible for performing, or hiring necessary personnel to perform, all necessary maintenance and repairs to the Property. ',
            ['obligations.ob_repair']
        ),
        'reimburse_maintenance': TemplateObj(
            'The Owner shall reimburse the Manager for the cost of all such maintenance and repairs. ',
            ['obligations.ob_reimburse_maintenance']
        ),
        'repair_invoice': TemplateObj(
            'The Manager shall provide the Owner invoices of the actual costs.',
            ['obligations.ob_repair_invoice']
        ),
        'legal_proceedings': TemplateObj(
            '[CONDITION_A] The Manager shall handle all legal proceedings.',
            ['obligations.ob_legal_proceedings']
        ),
        # 'termination_notice': TemplateObj(
        #     'This Agreement may be terminated at any time by either Party upon X days written notice to the other Party. ',
        #     [
        #         'powers.pow_terminate_notice_owner', 
        #         'powers.pow_terminate_notice_manager'
        #     ]
        # ),
        'disburse_termination': TemplateObj(
            '[CONDITION_B] the Manager shall disburse to the Owner any monies in the Manager\'s possession due and owing to the Owner [REFINEMENT_A]. ',
            ['obligations.ob_disburse_termination']
        ),
        # TODO: We have a case of "prior to" that isnt used as a refinement
        'reimburse_termination': TemplateObj(
            'The Owner shall reimburse the Manager for any expenses incurred or approved prior to the date of termination [REFINEMENT_B].',
            ['obligations.ob_reimburse_termination']
        )
    }
)

# TODO: May set it up so that ANY obligation can have a refinement...could be a condition or a refinement
## Would depend on the frame induced by the CNL
## User selects an obligation instead of a parameter. No need for parameters
## Would need something that keeps track of all of it. Actually wouldnt be too hard.
## Might even allow me to get rid of the parameter config...


parameters: Dict[str, ParameterSpec] = {
    'CONDITION_A': ParameterSpec(
        op_codes = [ParmOpCode.ADD_TRIGGER],
        configs= [
            ParameterConfig(
                norm_type = 'obligations',
                norm_id = 'ob_legal_proceedings',
                norm_component = 'trigger',
                dm_obj_type='',
                dm_obj_name='',
            )
        ]
    ),

    'CONDITION_B': ParameterSpec(
        op_codes = [ParmOpCode.ADD_TRIGGER],
        configs = [
            ParameterConfig(
                norm_type = 'obligations',
                norm_id = 'ob_disburse_termination',
                norm_component = 'trigger',
                dm_obj_type='',
                dm_obj_name='',
            )
        ]
    ),

    'REFINEMENT_A': ParameterSpec(
        op_codes = [ParmOpCode.REFINE_PREDICATE],
        configs = [
            ParameterConfig(
                norm_type = 'obligations',
                norm_id = 'ob_disburse_termination',
                norm_component = 'consequent',
                dm_obj_type='events',
                dm_obj_name='evt_disburse_termination'
            )
        ]
    ),

    'REFINEMENT_B': ParameterSpec(
        op_codes = [ParmOpCode.REFINE_PREDICATE],
        configs = [
            ParameterConfig(
                norm_type = 'obligations',
                norm_id = 'ob_reimburse_termination',
                norm_component = 'consequent',
                dm_obj_type='events',
                dm_obj_name='evt_reimburse_termination'
            )
        ]
    )
}