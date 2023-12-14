def rec_print_folders(n: int, pref: str, root: list) -> None:
    '''
    This function prints the contents of a given root folder with indentations.
    '''
    # base case: if root is empty, return
    if not root:
        return
    # recursive case: loop through the elements of root
    for elem in root:
        # if elem is a file, print it with - and pref
        if isinstance(elem, str):
            print(pref + '-' + elem)
        # if elem is a folder, print it with > and pref, and increase n by 1
        elif isinstance(elem, list):
            print(pref + '>Folder_' + str(n))
            rec_print_folders(n + 1, pref + '-', elem)


def rec_count_files(root: list) -> int:
    '''
    The functions counts number of files in a given folder (and all its sub-folders).
    :param root: A nested list: an element either is a file (name) or a list as a sub-folder.
    :return:
    '''
    # base case: if root is empty, return 0
    if not root:
        return 0
    # recursive case: loop through the elements of root
    count = 0
    for elem in root:
        # if elem is a file, increase count by 1
        if isinstance(elem, str):
            count += 1
        # if elem is a folder, add the count of its files to the total count
        elif isinstance(elem, list):
            count += rec_count_files(elem)
    return count


if __name__ == "__main__":
    test_cases = [
        ['file_1', []],
        ['file_1', 'file_2', ['file_1']],
        ['file_1', 'file_2', ['file_3', 'file_4', 'file_5'], ['file_6', ['file_7', 'file_8'], ['file_9'],
                                                              'file_9', ['file_10']], []],
        ['file_1', ['file_3', ['file_2', ['file_10', ['file_9', 'file_8']]]], []],
        [[], [[], [[]]]]
    ]

    for case in test_cases:
        rec_print_folders(0, '', case)
        print('Number of files in case: ', case, ' is ', rec_count_files(case))