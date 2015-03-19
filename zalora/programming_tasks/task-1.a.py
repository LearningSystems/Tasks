def convert_data_lists_of_lists_as_single_data_list(complex_array):
    data_list = []
    for value_list in complex_array:
        data_list.extend(value_list)
    return data_list


def print_items_of_list_by_separating_lines(simple_array):
    if simple_array:
        for item in simple_array:
            print item


def wrapper_method_for_process(complex_array):
    data_list = convert_data_lists_of_lists_as_single_data_list(complex_array)
    print_items_of_list_by_separating_lines(simple_array=data_list)


if __name__ == "__main__":
    array = [['a', 'b', 'c'], ['d', 'e', 'f']]
    wrapper_method_for_process(array)
