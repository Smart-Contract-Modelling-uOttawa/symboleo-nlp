class Particle:
    def to_sym(self):
        raise NotImplementedError()


class VariableDotExpression(Particle):
    def __init__(self, name: str):
        self.name = name
    
    def to_sym(self):
        return self.name


class TimeValue:
    def to_sym(self):
        raise NotImplementedError()

class TimeValueInt(TimeValue):
    def __init__(self, value: int):
        self.value = value
    
    def to_sym(self):
        return self.value

class TimeValueVariable(TimeValue):
    def __init__(self, variable: VariableDotExpression):
        self.variable = variable
    
    def to_sym(self):
        return self.variable.to_sym()

## Make this an enum...
# TimeUnit:
# 	'seconds' | 'minutes' | 'hours' | 'days' | 'weeks' | 'months' | 'years';

    