from app.classes.spec.nl_template import NLTemplate, TemplateObj

nl_template = NLTemplate(
    template_dict = {
        'pay_deposit': TemplateObj(
            'The renter must pay a security deposit of $1000 within 2 weeks of occupying the property.'
        ),
        'no_pets': TemplateObj(
            'The renter may not keep any pets on the property unless authorization is provided by the landlord '
        ),
        'pay_extra': TemplateObj(
            'In the event of a late payment, the renter must pay an extra fee of $50.'
        ),
    }
)
