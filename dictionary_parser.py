from file_helper import FileHelper
from definition_parser import DefinitionParser


class DictionaryParser:

    DEFINITIONS_DIR = 'extracted_definitions/'
    DICTIONARY_DIR = 'raw_dictionary/'

    @staticmethod
    def parse_dictionary():
        definition_filename = DictionaryParser.DEFINITIONS_DIR + 'postbase_definitions.csv'
        misc_filename = DictionaryParser.DEFINITIONS_DIR + 'postbase_misc.csv'
        dictionary_filename = DictionaryParser.DICTIONARY_DIR + 'postbases.txt'

        file_contents = FileHelper.read_file(dictionary_filename)
        parser = DefinitionParser(file_contents)
        definitions, misc = parser.get_definitions_and_misc_as_csv()
        FileHelper.write_to_csv(definition_filename, definitions)
        FileHelper.write_to_csv(misc_filename, misc)
        for content in definitions:
            print(content)


if __name__ == '__main__':
    DictionaryParser.parse_dictionary()
