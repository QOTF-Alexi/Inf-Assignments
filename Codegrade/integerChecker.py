def is_integer(checkInt):
    try:
        checkInt = int(checkInt)
        print("Valid integer")
        return True
    except ValueError:
        print("Invalid integer")
        return False


if __name__ == "__main__":
    checkInt = input("Enter a string to check: ")
    is_integer(checkInt)