
init_state_dicts = {
    'obligation_states': {
        'create': 'create.v.02',
        'discharge': 'free.v.06',
        'active': 'trip.v.04',
        'in_effect': 'effect.v.02',
        'suspension': 'suspend.v.06',
        'violation': 'transgress.v.01',
        'fulfillment': 'satisfy.v.01',
        'unsuccessful_termination': 'end.v.02'
    },

    'contract_states': {
        'form': 'create.v.02',
        'active': 'trip.v.04',
        'unassign': 'exempt.v.01',
        'in_effect': 'effect.v.02',
        'suspension': 'suspend.v.06',
        'rescission': 'revoke.v.02',
        'unsuccessful_termination': 'end.v.02',
        'successful_termination': 'succeed.v.01'
    },

    'power_states': {
        'create': 'create.v.02',
        'active': 'trip.v.04',
        'in_effect': 'effect.v.02',
        'suspension': 'suspend.v.06',
        'unsuccessful_termination': 'end.v.02',
        'successful_termination': 'succeed.v.01'
    }

}