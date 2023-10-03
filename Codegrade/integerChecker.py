not_allowed = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm,./<>?`~!@#$%^&*()_+=[]{}|;:\'\""


def is_integer(unchecked):
    try:
        unchecked = int(unchecked)
        print("Valid integer")
        return True
    except ValueError:
        print("Invalid integer")
        return False


def remove_non_integer(unchecked):
    print(int(unchecked.translate({ord(i): None for i in not_allowed})))


if __name__ == "__main__":
    unchecked = input("Enter a string to check: ")
    is_integer(unchecked)
    remove_non_integer(unchecked)