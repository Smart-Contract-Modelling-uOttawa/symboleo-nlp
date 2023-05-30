from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.parameter_config import ParameterConfig

nl_template = NLTemplate(
    template_dict = {
        'legal_proceedings': TemplateObj(
            '[P1] The Manager shall handle all such legal proceedings',
            {
                'P1': [ParameterConfig('obligations', 'ob_legal_proceedings', 'antecedent')]
            }
        ),
        'disburse_termination': TemplateObj(
            '[P1] the Manager shall disburse to the Owner any monies in the Manager\'s possession due and owing to the Owner [P2]',
            {
                'P1': [ParameterConfig('obligations', 'ob_disburse_termination', 'antecedent')],
                'P2': [ParameterConfig('obligations', 'ob_disburse_termination', 'consequent')]
            }
        ),
        'reimburse_termination': TemplateObj(
            'The Owner shall reimburse the Manager for any expenses incurred or approved prior to the date of termination [P2]',
            {
                'P2': [ParameterConfig('obligations', 'ob_reimburse_termination', 'consequent')]
            }
        )
    }
)
