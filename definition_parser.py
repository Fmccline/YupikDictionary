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
            definition_entry = self.get_definition_entry(line_number)
            definition = definition_entry.to_list()
            if definition_entry.def_type == definition_entry.MISC:
                misc.append(definition)
            else:
                definitions.append(definition)
        return definitions, misc

    def get_definition_entry(self, line_number):
        words = self.lines[line_number]
        words = words.replace('\n', ' ')
        words = words.split(' ')
        phrase, word_number = self.get_phrase(words)
        if word_number <= 0 or word_number >= len(words) - 1:
            definition, word_number = self.get_definition(words, word_number)
            if definition == '':
                definition_type = DefinitionEntry.MISC
            else:
                definition_type = DefinitionEntry.DEFINITION
            definition_entry = DefinitionEntry(line_number, phrase, definition_type)
            definition_entry.definition = definition
            return definition_entry

        definition, word_number = self.get_definition(words, word_number)
        extra = ''
        for word_num in range(word_number, len(words)):
            word = words[word_num]
            if word[-1] == self.CLOSING_QUOTE:
                continue
            extra = words[word_num] + ' '

        definition_type = DefinitionEntry.DEFINITION
        if self.is_postbase(phrase):
            definition_type = DefinitionEntry.POSTBASE

        definition_entry = DefinitionEntry(line_number, phrase, definition_type)
        definition_entry.definition = definition
        definition_entry.extra = extra
        return definition_entry

    def get_phrase(self, words):
        phrase = ''
        for word_num in range(len(words)):
            word = words[word_num]
            if word[0] == self.OPENING_QUOTE:
                break
            else:
                phrase += word + ' '
        return phrase[:-1], word_num  # for some reason a space is appended to end of phrase

    def get_definition(self, words, starting_word):
        definition = ''
        possibly_defined = False
        is_defining = False
        for word_num in range(starting_word, len(words)):
            word = words[word_num]
            if word[0] == self.OPENING_QUOTE:
                is_defining = True
                if word[-1] == self.CLOSING_QUOTE:
                    definition += word[1:-1]
                    break
                else:
                    definition += word[1:] + ' '
            elif word[-1] == self.CLOSING_QUOTE:
                definition += word[:-1]
                possibly_defined = True
            elif possibly_defined:
                if word[0].isalpha():
                    definition += self.CLOSING_QUOTE + word + ' '
                else:
                    break
            elif is_defining:
                definition += word + ' '
        return definition, word_num

    def is_postbase(self, phrase):
        # words = phrase.split(' ')
        # if len(words) > 1:
        #     return False
        return phrase[-1] == '-'
