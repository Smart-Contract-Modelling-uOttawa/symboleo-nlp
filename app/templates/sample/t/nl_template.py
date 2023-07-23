from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.parameter_config import ParameterConfig

nl_template = NLTemplate(
    template_dict = {
        'pay_deposit': TemplateObj(
            'The renter must pay a security deposit of $1000 [P1]',
            {
                'P1': [ ParameterConfig('obligations', 'ob_pay_deposit', 'consequent')]
            }
        ),
        'no_pets': TemplateObj(
            'The renter may not keep any pets on the property [P2]',
            {
                'P2': [ ParameterConfig('obligations', 'ob_no_pets', 'consequent')]
            }
        ),
        'late_payment': TemplateObj(
            '[P3] the renter must pay an extra fee of $50',
            {
                'P3': [ ParameterConfig('obligations', 'ob_pay_extra', 'antecedent')]
            }
        ),
        # Kill
        'test_cond': TemplateObj(
            'if something happens [P4], the renter must pay an extra fee of $50',
            {
                'P4': [ ParameterConfig('obligations', 'ob_test', 'antecedent')]
            }
        ),
    }
)
