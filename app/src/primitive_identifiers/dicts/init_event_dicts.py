class EventDictValue:
    def __init__(self, synset_name, custom_list = []):
        self.synset_name = synset_name
        self.custom_list = custom_list

init_event_dicts = {
    'obligation': {
        'triggered': EventDictValue('trip.v.04'),
        'activated': EventDictValue('activate.v.02'),
        'suspended': EventDictValue('suspend.v.06'), 
        'resumed': EventDictValue('resume.v.02'), 
        'discharged': EventDictValue('free.v.06'), 
        'expired': EventDictValue('run_out.v.04'), 
        'fulfilled': EventDictValue('satisfy.v.01', ['complete']), 
        'violated': EventDictValue('transgress.v.01'), 
        'terminated': EventDictValue('end.v.02')
    },

    'contract': {
        'activated': EventDictValue('activate.v.02'), 
        'suspended': EventDictValue('suspend.v.06'), 
        'resumed': EventDictValue('resume.v.02'),
        'fulfilled_obligations': EventDictValue('satisfy.v.01'),
        'revoked_party': EventDictValue('revoke.v.02'),
        'assigned_party': EventDictValue('delegate.v.02'),
        'terminated': EventDictValue('end.v.02'),
        'rescinded': EventDictValue('revoke.v.02')
    },

    'power': {
        'triggered': EventDictValue('trip.v.04'), 
        'activated': EventDictValue('activate.v.02'), 
        'suspended': EventDictValue('suspend.v.06'), 
        'resumed': EventDictValue('resume.v.02'), 
        'exerted': EventDictValue('exert.v.01'), 
        'expired': EventDictValue('run_out.v.04'),
        'terminated': EventDictValue('end.v.02')
    }
}