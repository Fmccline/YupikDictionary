from definitionentry import DefinitionEntry


class DefinitionParser:

    OPENING_QUOTE = '\N{LEFT SINGLE QUOTATION MARK}'
    CLOSING_QUOTE = '\N{RIGHT SINGLE QUOTATION MARK}'

    def __init__(self, data):
        self.lines = data.split('\n\n')
        self.line_number = 0

    def get_definitions_and_misc_as_csv(self):
        definitions, misc = [], []
        for line_number in range(len(self.lines)):
            definition_entry = self.get_definitions(line_number)
            definition = definition_entry.to_csv()
            if definition_entry.type == definition_entry.MISC:
                misc.append(definition)
            else:
                definitions.append(definition)
        return definitions, misc

    def get_definitions(self, line_number):
        current_line = self.lines[line_number]
        words = current_line.split(' ')
        definition = current_line
        extra = ''
        if self.is_definition(words):
            definition, extra = self.get_definition(words[1:])
            first_word = words[0]
            definition_type = DefinitionEntry.POSTBASE if first_word[-1] is '-' else DefinitionEntry.DEFINITION
        else:
            definition_type = DefinitionEntry.MISC
        definition_entry = DefinitionEntry(line_number)
        definition_entry.type = definition_type
        definition_entry.definition = definition
        definition_entry.extra = extra
        return definition_entry

    def is_definition(self, words):
        if len(words) < 2:
            return False
        first_word = words[0]
        second_word = words[1]
        return first_word[-1] == '-' or second_word[0] == self.OPENING_QUOTE

    def get_definition(self, words):
        definition = ''
        extra = ''
        is_defined = False
        for word in words:
            if is_defined:
                extra += word + ' '
            elif word[0] == self.OPENING_QUOTE:
                definition += word[1:] + ' '
            elif word[len(word) - 1] == self.CLOSING_QUOTE:
                definition += word[0:len(word) - 1]
                is_defined = True
            else:
                definition += word + ' '
        return definition, extra
