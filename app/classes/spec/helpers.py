class Particle:
    def to_sym(self):
        raise NotImplementedError()


class VariableDotExpression(Particle):
    def __init__(self, name: str = ''):
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

class TimeUnit:
    def to_sym(self):
        raise NotImplementedError()

class TimeUnitStr(TimeUnit):
    def __init__(self, unit: str):
        self.unit = unit # 'seconds' | 'minutes' | 'hours' | 'days' | 'weeks' | 'months' | 'years';
    
    def to_sym(self):
        return self.unit

class TimeValueVariable(TimeValue):
    variable = VariableDotExpression()
    
    def __init__(self, variable: VariableDotExpression):
        self.variable = variable
    
    def to_sym(self):
        return self.variable.to_sym()

## Make this an enum...
# TimeUnit:
# 	'seconds' | 'minutes' | 'hours' | 'days' | 'weeks' | 'months' | 'years';

    