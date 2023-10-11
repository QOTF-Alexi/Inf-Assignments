letters = "qwertyuiopasdfghjklzxcvbnm"
validChars = "1234567890*@!?" + letters + letters.upper()


def checkPW(passwd):
    checkPass = set(passwd)
    if 8 <= len(passwd) <= 20:
        if len(checkPass.difference(validChars)) == 0:
            return True
    else:
        return False


if __name__ == "__main__":
    attempts = 3
    while attempts > 0:
        passwd = input("Password: ")
        validity = checkPW(passwd)
        if validity:
            print("Password is valid")
            attempts = 0
        else:
            print("Password is invalid")
            attempts -= 1