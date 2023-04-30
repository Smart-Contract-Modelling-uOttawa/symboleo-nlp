from app.classes.spec.declaration import Declaration, DeclarationProp
from app.src.sym_updaters.common_event.i_map_common_events import IMapCommonEvents
from app.classes.template_event.common_event import CommonEvent

class ProvideTerminationMapper(IMapCommonEvents):
    def map(self, evt: CommonEvent) -> Declaration:
        # TODO: Figure out how to customize num days in the  adverb
        # Perhaps use a default value, and the user can just alter it...?

        return Declaration(
            f'evt_provide_notice_{evt.subj.to_text()}',
            'ProvideTerminationNotice',
            'events',
            [
                DeclarationProp('agent', evt.subj.to_text(), 'Role'),
                DeclarationProp('num_days', 'X', 'Number')
            ]
        )