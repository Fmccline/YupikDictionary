

class DefinitionEntry:

    DEFINITION = 'DEF'
    POSTBASE = 'POST'
    MISC = 'MISC'

    def __init__(self, line_number, phrase, def_type):
        self.line_number = line_number
        self.phrase = phrase
        self.def_type = def_type
        self.definition = ''
        self.extra = ''

    def is_mis(self):
        return self.def_type == self.MISC

    def to_list(self):
        return [self.line_number, self.def_type, self.phrase, self.definition, self.extra]

