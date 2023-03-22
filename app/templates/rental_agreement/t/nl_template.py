from typing import Dict, List
from app.src.operations.configs import ParameterConfig, ParameterSpec, OpCode
from app.classes.nl_template import NLTemplate, TemplateObj

rental_nl_template = NLTemplate(
    template_dict = {
        'pay_rent': TemplateObj(
            'The monthly rent to be paid by the Renter to the Landlord is (monthly_rent). It is to be paid by the Renter before the first day of every month, such that the first rent payment is due on (first_rent_due_date).',
            ['obligations.pay_rent']
            # Will probably add a refinement here... need to figure out frequency
        ),
        'late_payment': TemplateObj(
            '[LATE_PAYMENT_CONDITION] the Landlord is entitled to impose a (late_fine) fine as late fee. ',
            ['obligations.late_payment']
        ),
        'pay_security_deposit': TemplateObj(
            '[SECURITY_DEPOSIT_REFINEMENT] the Renter will pay the Landlord an amount of (security_deposit_amount) as a security deposit to cover the cost of any damages suffered by the premises and cleaning.',
            ['obligations.pay_security_deposit']
        ),
        'return_deposit': TemplateObj(
            'Such security deposit will be returned to the Renter [RETURN_DEPOSIT_CONDITION], provided the premises are left in the same condition as prior to the occupancy.',
            ['obligations.return_deposit']
            # Might add further antecedents...?
        ),
        'no_pets': TemplateObj(
            'The Parties agree that the Renter will not keep any pets on the premises [PETS_UNLESS_CONDITION].',
            ['obligations.no_pets'] # Does this make sense...?
        ),
        
        ## Remove all absolute termination powers
        # 'terminate_breach': TemplateObj(
        #     'This Agreement may be terminated in the event that any of the following occurs: 1. Immediately [TERMINATION_CONDITION1]',
        #     ['powers.terminate_breach1', 'powers.terminate_breach2']
        # ),
        # 'terminate_notice': TemplateObj(
        #     'This Agreement may be terminated in the event that any of the following occurs: 2. At any given time [TERMINATION_CONDITION2]',
        #     ['powers.terminate_notice']
        # ),
        # 'terminate_abandon': TemplateObj(
        #     '[TERMINATION_CONDITION3], the Landlord will be entitled to enter the Premises by any means without facing any liability and the Landlord may terminate this Agreement.',
        #     ['powers.terminate_abandon']
        # )
    }
)

# Needs to be a list; since a parameter can have multiple impacts
parameters: Dict[str, ParameterSpec] = {
    'PAY_RENT_REFINEMENT': ParameterSpec(
        op_codes = [OpCode.REFINE_PREDICATE],
        configs= [
            ParameterConfig(
                norm_type = 'obligations',
                norm_id = 'pay_rent',
                norm_component = 'consequent',
                dm_obj_type='events',
                dm_obj_name='evt_pay_rent',
            )
        ]
    ),

    'LATE_PAYMENT_CONDITION': ParameterSpec(
        op_codes = [OpCode.ADD_TRIGGER],
        configs = [
            ParameterConfig(
                norm_type = 'obligations',
                norm_id = 'late_payment',
                norm_component = 'consequent',
                dm_obj_type='events',
                dm_obj_name='evt_pay_late_fine',
            )
        ]
    ),

    'SECURITY_DEPOSIT_REFINEMENT': ParameterSpec(
        op_codes = [OpCode.ADD_TRIGGER, OpCode.REFINE_PREDICATE],
        configs = [
            ParameterConfig(
                norm_type = 'obligations',
                norm_id = 'pay_security_deposit',
                norm_component = 'consequent',
                dm_obj_type='events',
                dm_obj_name='evt_pay_deposit'
            )
        ]
    ),

    'RETURN_DEPOSIT_REFINEMENT': ParameterSpec(
        op_codes = [OpCode.ADD_TRIGGER, OpCode.REFINE_PREDICATE],
        configs = [
            ParameterConfig(
                norm_type = 'obligations',
                norm_id = 'return_deposit',
                norm_component = 'consequent',
                dm_obj_type='events',
                dm_obj_name='evt_return_deposit'
            )
        ]
    ),

    'PETS_UNLESS_CONDITION': ParameterSpec(
        op_codes = [OpCode.ADD_NORM],
        configs = [
            ParameterConfig(
                norm_type = 'obligations',
                norm_id = 'no_pets',
                norm_component = 'consequent',
                dm_obj_type='events',
                dm_obj_name='evt_keep_pets'
            )
        ]
    ),

    # Need a better way to do these termination conditions
    ## In broad form, they are basically the same
    # So we'd want to list a bunch of options... maybe add in disjuncts
    'TERMINATION_CONDITION1': ParameterSpec(
        op_codes = [OpCode.ADD_TRIGGER],
        configs = [
            ParameterConfig(
                norm_type = 'powers',
                norm_id = 'terminate_breach1',
                norm_component = 'trigger',
                dm_obj_type='',
                dm_obj_name=''
            ),
            ParameterConfig(
                norm_type = 'powers',
                norm_id = 'terminate_breach2',
                norm_component = 'trigger',
                dm_obj_type='',
                dm_obj_name=''
            ),
        ]
    )
}