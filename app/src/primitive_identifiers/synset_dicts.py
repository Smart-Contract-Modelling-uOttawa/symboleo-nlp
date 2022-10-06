synset_dicts = {
    'obligation_events': {
        'triggered': 'trip.v.04', 
        'activated': 'activate.v.02', 
        'suspended': 'suspend.v.06', 
        'resumed': 'resume.v.02', 
        'discharged': 'free.v.06', 
        'expired': 'run_out.v.04', 
        'fulfilled': 'satisfy.v.01', 
        'violated': 'transgress.v.01', 
        'terminated': 'end.v.02'
    },

    'contract_events': {
        'activated': 'activate.v.02', 
        'suspended': 'suspend.v.06', 
        'resumed': 'resume.v.02',
        'fulfilled_obligations': 'satisfy.v.01',
        'revoked_party': 'revoke.v.02',
        'assigned_party': 'delegate.v.02',
        'terminated': 'end.v.02',
        'rescinded': 'revoke.v.02'
    },

    'power_events': {
        'triggered': 'trip.v.04', 
        'activated': 'activate.v.02', 
        'suspended': 'suspend.v.06', 
        'resumed': 'resume.v.02', 
        'exerted': 'exert.v.01', 
        'expired': 'run_out.v.04',
        'terminated': 'end.v.02'
    },

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