from app.src.nl_creator.nl_fillers.nl_unit_filler_dict import NLUnitFillerDictConstructor
from app.src.nl_creator.nl_creator import NLCreator

class NLCreatorBuilder:
    @staticmethod
    def build():
        nl_filler_dict = NLUnitFillerDictConstructor.build()
        
        return NLCreator(
            nl_filler_dict
        )
