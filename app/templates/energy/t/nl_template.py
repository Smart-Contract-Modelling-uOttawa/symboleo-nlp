from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.parameter_config import ParameterConfig, PatternClassType

nl_template = NLTemplate(
    template_dict = {
        'dispatch_energy': TemplateObj(
            'Prosumer shall dispatch <energy_qnt> kW of power to the Buyer [P1]',
            {
                'P1': [ParameterConfig('obligations', 'ob_dispatch', 'consequent')]
            }
        ),
        'dispatch_location': TemplateObj(
            'The power needs to be dispatched to <location>.'
        ),
        'payment': TemplateObj(
            'The Buyer shall pay <amount> in CAD to the Prosumer [P2]',
            {
                'P2': [ParameterConfig('obligations', 'ob_payment', 'consequent')]
            }
        ),
        'late_payment': TemplateObj(
            '[P3], the Buyer shall pay a late fee equal to <percentage> of the amount owed, and the Seller may suspend performance of all of its obligations under the agreement until payment of amounts owed has been received in full.'
        ),
        'termination': TemplateObj(
            'Any delay in the dispatching of power, or any problem with the voltage (which must be between <min> V and <max> V), will entitle the Buyer to terminate the contract.'
        ),
    }
)


