from typing import Dict
from app.src.operations.configs import ParameterConfig, OpCode

nl_template = {
    'obligations': {
        'delivery': 'The Seller shall deliver the Order in one delivery to the Buyer [DELIVERY_REFINEMENT]',
        'payment': 'The Buyer shall pay (payment_amount) to the Seller [PAYMENT_REFINEMENT].',
        'latePayment': '[LATE_PAYMENT_CONDITION], the Buyer shall pay interests equal to (interest_amount) percent of the payment amount'
    },
    'surviving_obligations': {
         'disclosure': 'Both Seller and Buyer must keep the contents of this contract confidential [CONFIDENTIALITY_REFINEMENT]',
    },
    'powers': {
        'suspendDelivery': '[DELIVERY_SUSPENSION_CONDITION] the Seller may suspend performance of all of its obligations under the agreement [DELIVERY_RESUMPTION_TRIGGER]',
        'resumeDelivery': '[DELIVERY_SUSPENSION_CONDITION] the Seller may suspend performance of all of its obligations under the agreement [DELIVERY_RESUMPTION_TRIGGER]',
        'terminateContract': 'Any delay in delivery of the goods will not entitle the Buyer to terminate the Contract [TERMINATION_REFINEMENT]'
    }
}

sample_customization = [
    ('DELIVERY_REFINEMENT', 'before delivery due date'),
    ('PAYMENT_REFINEMENT', 'before payment due date'),
    ('LATE_PAYMENT_CONDITION', 'if payment is not completed'),
    ('CONFIDENTIALITY_REFINEMENT', 'until 6 months after contract termination'),
    ('DELIVERY_SUSPENSION_CONDITION', 'if payment is not completed'),
    ('DELIVERY_RESUMPTION_CONDITION', 'until payment is completed'),
    ('TERMINATION_CONDITION', 'unless such delay exceeds 10 Days') # Has a coreference... more difficult
]

# TODO: Will need to fix these up with the proper values and test them all out
# TODO: Wil need a more formal way of linking the NL to the corresponding norms
parameters: Dict[str, ParameterConfig] = {
    'DELIVERY_REFINEMENT': ParameterConfig(
        norm_type = 'obligations',
        norm_id = 'delivery',
        norm_component = 'consequent',
        dm_obj_type='events',
        dm_obj_name='delivered',
        op_codes = [OpCode.REFINE_PREDICATE],
    ),
    'PAYMENT_REFINEMENT': ParameterConfig(
        norm_type = 'obligations',
        norm_id = 'payment',
        norm_component = 'consequent',
        dm_obj_type='events',
        dm_obj_name='delivered',
        op_codes = [OpCode.REFINE_PREDICATE],
    ),
    'LATE_PAYMENT_CONDITION': ParameterConfig(
        norm_type = 'obligations',
        norm_id = 'latePayment',
        norm_component = 'trigger',
        dm_obj_type='events',
        dm_obj_name='paidLate',
        op_codes = [OpCode.ADD_TRIGGER],
    ),
    'CONFIDENTIALITY_REFINEMENT': ParameterConfig(
        norm_type = 'surviving_obligations',
        norm_id = 'disclosure',
        norm_component = 'consequent',
        dm_obj_type='events',
        dm_obj_name='disclosed',
        op_codes = [OpCode.REFINE_PREDICATE],
    ),
    'DELIVERY_SUSPENSION_CONDITION': ParameterConfig(
        norm_type = 'powers',
        norm_id = 'suspend_delivery',
        norm_component = 'trigger',
        dm_obj_type='events',
        dm_obj_name='XX',
        op_codes = [OpCode.ADD_TRIGGER],
    ),
    'DELIVERY_RESUMPTION_CONDITION': ParameterConfig(
        norm_type = 'powers',
        norm_id = 'resume_delivery',
        norm_component = 'trigger',
        dm_obj_type='events',
        dm_obj_name='XX',
        op_codes = [OpCode.ADD_TRIGGER],
    ),
    'TERMINATION_CONDITION': ParameterConfig(
        norm_type = 'powers',
        norm_id = 'terminateContract',
        norm_component = 'trigger',
        dm_obj_type='events',
        dm_obj_name='XX',
        op_codes = [OpCode.ADD_TRIGGER],
    )
}