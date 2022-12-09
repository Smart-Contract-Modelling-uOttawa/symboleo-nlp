class IBuildRolePatterns:
    def build(self, role_name:str):
        raise NotImplementedError()

class RolePatternBuilder(IBuildRolePatterns):
    def build(self, role_name: str):
        role_pattern = [
                [{ "POS": { "IN": ["NOUN", "PROPN"]}, "LOWER": role_name }]
            ]
        return role_pattern