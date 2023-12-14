def find_in_list(n, lst):
    # loop through the list
    for item in lst:
        # if the item is equal to the element, return True
        if item == n:
            return True
    # if the loop ends without finding the element, return False
    return False


def rec_find_in_list(n, lst):
    # base case: the list is empty, return False
    if len(lst) == 0:
        return False
    # recursive case: check the first element of the list and the rest of the list
    else:
        # if the first element is equal to the element, return True
        if lst[0] == n:
            return True
        # otherwise, return the result of calling rec_contains with the element and the rest of the list
        else:
            return rec_find_in_list(n, lst[1:])


if __name__ == "__main__":
    toFind = input("Enter a criterium: ")
    lst = list(input("Enter a list: "))
    print(find_in_list(toFind, lst))
    print(rec_find_in_list(toFind, lst))
