import os
from collections import Counter

"""
Took assumptions as
1. urban TEE and Looney Tunes @ urban TEE as differnt brands

If assumption is wrong we can solve problem in other way also
"""


class CsvFileReaderReturnRequired():
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def get_brand_names_and_words_counter(self):
        data_list = []
        words_counter = Counter()
        with open(self.csv_file, 'r') as csv_file:
            for row in csv_file.readlines():
                base_raw_row_data = row[2:-3]
                intermediate_row_data = base_raw_row_data.split(',')
                words_counter.update(intermediate_row_data)
                data_list.extend(intermediate_row_data)
        brand_names = set(data_list)
        return brand_names, words_counter


if __name__ == "__main__":

    try:
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data_files', 'top10_sample.csv')
    except IOError:
        print "File path Provided is not correct"
    reader = CsvFileReaderReturnRequired(file_path)
    brand_names, words_counter = reader.get_brand_names_and_words_counter()
    print words_counter
