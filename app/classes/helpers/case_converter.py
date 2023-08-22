from re import sub

class CaseConverter:
    @staticmethod
    def to_pascal(s: str):
        res = s.replace("_", " ").title().replace(" ", "")
        return res

    @staticmethod
    def to_snake(s: str):
        return '_'.join(
            sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
            str(s).replace('-', ' '))).split()).lower()
    