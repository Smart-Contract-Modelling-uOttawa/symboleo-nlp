from typing import Dict, List
from app.src.operations.parm_operations.configs import ParameterConfig, ParameterSpec, ParmOpCode
from app.classes.nl_template import NLTemplate, TemplateObj

# TODO: Might include the parameters in this object as well...
sample_nl_template = NLTemplate(
    template_dict = {
        'delivery': TemplateObj(
            'The Seller shall deliver the Order in one delivery to the Buyer [DELIVERY_REFINEMENT]',
            ['obligations.delivery']
        ),
        'payment': TemplateObj(
            'The Buyer shall pay (payment_amount) to the Seller [PAYMENT_REFINEMENT].',
            ['obligations.payment']
        ),
        'latePayment': TemplateObj(
            '[LATE_PAYMENT_CONDITION], the Buyer shall pay interests equal to (interest_amount) percent of the payment amount',
            ['obligations.latePayment']
        ),
        'disclosure': TemplateObj(
            'Both Seller and Buyer must keep the contents of this contract confidential [CONFIDENTIALITY_REFINEMENT]',
            ['surviving_obligations.so1', 'surviving_obligations.so2']
        ),
        'suspendResumeDelivery': TemplateObj(
            '[DELIVERY_SUSPENSION_CONDITION] the Seller may suspend performance of all of its obligations under the agreement until payment is completed',
            ['powers.suspendDelivery']
        ),
        'terminateContract': TemplateObj(
            'Any delay in delivery of the goods will not entitle the Buyer to terminate the Contract [TERMINATION_EXCEPTION]',
            ['powers.terminateContract']
        )
    }
)

# Needs to be a list; since a parameter can have multiple impacts
parameters: Dict[str, ParameterSpec] = {
    # before [DELIVERY_DUE_DATE]
    # BEFORE DOMAIN_DATE(delivery.delDueD)
    # TODO: Requires a BEFORE TIMEPOINT frame
    'DELIVERY_REFINEMENT': ParameterSpec(
        op_codes = [ParmOpCode.REFINE_PREDICATE, ParmOpCode.ADD_TRIGGER],
        configs= [
            ParameterConfig(
                norm_type = 'obligations',
                norm_id = 'delivery',
                norm_component = 'consequent',
                dm_obj_type='events',
                dm_obj_name='delivered',
            )
        ]
    ),

    # before [PAYMENT_DUE_DATE]
    # BEFORE DOMAIN_DATE(payment.payDueDate)
    'PAYMENT_REFINEMENT': ParameterSpec(
        op_codes = [ParmOpCode.REFINE_PREDICATE, ParmOpCode.ADD_TRIGGER],
        configs = [
            ParameterConfig(
                norm_type = 'obligations',
                norm_id = 'payment',
                norm_component = 'consequent',
                dm_obj_type='events',
                dm_obj_name='paid',
            )
        ]
    ),

    # In the event of late payment of the amount owed due
    # IF EVENT(violate payment obligation)
    'LATE_PAYMENT_CONDITION': ParameterSpec(
        op_codes = [ParmOpCode.ADD_TRIGGER],
        configs = [
            ParameterConfig(
                norm_type = 'obligations',
                norm_id = 'latePayment',
                norm_component = 'trigger',
                dm_obj_type='events',
                dm_obj_name='paidLate'
            )
        ]
    ),

    # for [CONFIDENTIALITY_MONTHS] months following the termination of the contract
    # Tough one - the "FOR TIMESPAN AFTER EVENT" frame only corresponds to HappensBefore if its a NOT
    # Can likely get away with using WITHIN
    # Also, this affects TWO norms... Maybe this needs to be a list of ParameterConfigs...
    'CONFIDENTIALITY_REFINEMENT': ParameterSpec(
        op_codes = [ParmOpCode.ADD_TRIGGER, ParmOpCode.REFINE_PREDICATE],
        configs = [
            ParameterConfig(
                norm_type = 'surviving_obligations',
                norm_id = 'so1',
                norm_component = 'consequent',
                dm_obj_type='events',
                dm_obj_name='disclosed'
            ),
            ParameterConfig(
                norm_type = 'surviving_obligations',
                norm_id = 'so2',
                norm_component = 'consequent',
                dm_obj_type='events',
                dm_obj_name='disclosed'
            )
        ]
    ),

    'DELIVERY_SUSPENSION_CONDITION': ParameterSpec(
        op_codes = [ParmOpCode.ADD_TRIGGER],
        configs = [
            ParameterConfig(
                norm_type = 'powers',
                norm_id = 'suspendDelivery',
                norm_component = 'trigger',
                dm_obj_type='',
                dm_obj_name=''
            )
        ]
    ),

    'TERMINATION_EXCEPTION': ParameterSpec(
        op_codes = [ParmOpCode.ADD_NORM],
        configs = [
            ParameterConfig(
                norm_type = 'powers',
                norm_id = 'terminateContract',
                norm_component = 'trigger',
                dm_obj_type='',
                dm_obj_name=''
            )
        ]
    )
}