from app.src.nlp.label_getter import IGetLabels

class FakeLabelGetter(IGetLabels):
    def __init__(self):
        self.__roles = [
            'partyA',
            'partyB',
        ]

    def get(self, str_val: str) -> str:
        if str_val in self.__roles:
            return self.__roles[str_val]
        
        return str_val.capitalize()