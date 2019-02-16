import csv


class FileHelper:

    @staticmethod
    def read_file(filename, encoding='utf-8'):
        with open(filename, encoding=encoding) as file:
            file_contents = file.read()
        return file_contents

    @staticmethod
    def write_definitions_to_csv(filename, postbases, encoding='utf-8', newline='', delimiter=','):
        with open(filename, 'w', encoding=encoding, newline=newline) as file:
            writer = csv.writer(file, delimiter=delimiter)
            for postbase in postbases:
                writer.writerow(postbase.to_csv_format())

    @staticmethod
    def write_to_csv(filename, rows, encoding='utf-8', newline='', delimiter=','):
        with open(filename, 'w', encoding=encoding, newline=newline) as file:
            writer = csv.writer(file, delimiter=delimiter)
            for row in rows:
                writer.writerow(row)
