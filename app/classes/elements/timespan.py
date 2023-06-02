class Timespan:
    def __init__(self, time_value, time_unit):
        self.time_unit = time_unit
        self.time_value = time_value
    
    def to_text(self):
        return f'{self.time_value} {self.time_unit}'