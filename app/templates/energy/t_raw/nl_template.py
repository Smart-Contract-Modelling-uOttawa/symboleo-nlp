from app.classes.spec.nl_template import NLTemplate, TemplateObj

nl_template = NLTemplate(
    template_dict = {
        'dispatch_energy': TemplateObj(
            'Prosumer shall dispatch <energy_qnt> kW of power to the Buyer, from <startTime> to <endTime>.'
        ),
        'dispatch_location': TemplateObj(
            'The power needs to be dispatched to <location>.'
        ),
        'payment': TemplateObj(
            'The Buyer shall pay <amount> in CAD to the Prosumer before <paydate>.'
        ),
        'lat_payment': TemplateObj(
            'In case of late payment, the Buyer shall pay a late fee equal to <percentage> of the amount owed, and the Seller may suspend performance of all of its obligations under the agreement until payment of amounts owed has been received in full.'
        ),
        'termination': TemplateObj(
            'Any delay in the dispatching of power, or any problem with the voltage (which must be between <min> V and <max> V), will entitle the Buyer to terminate the contract.'
        ),
    }
)


