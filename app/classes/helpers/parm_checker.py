import re

# Check if text is a contract spec parameter, e.g. [LIKE_THIS]
class ParmChecker:

    @staticmethod
    def is_parm(s:str) -> bool:
        pattern = r'\[([A-Z_]+)\]'
        match = re.match(pattern, s)
        return match 
    
    @staticmethod
    def lower_parm(s:str) -> str:
        return s[1:-1].lower()