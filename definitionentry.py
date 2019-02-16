

class DefinitionEntry:

    DEFINITION = 'DEF'
    POSTBASE = 'POST'
    MISC = 'MISC'

    def __init__(self, line_number):
        self.line_number = line_number
        self.definition = ''
        self.extra = ''
        self.type = self.MISC

    def is_mis(self):
        return self.type == self.MISC

    def to_csv(self):
        return [self.line_number, self.definition, self.extra]

