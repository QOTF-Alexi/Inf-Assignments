class PasswordManager:
    def __init__(self):
        self.old_passwords = []
        self.current = ""

    def get_password(__init__):
        print(__init__.current)

    def is_correct(__init__, attempt: str):
        if attempt == __init__.current:
            return True
        else:
            return False

    def set_password(__init__, newPass: str):
        if newPass not in __init__.old_passwords:
            __init__.current = newPass
            __init__.old_passwords.append(newPass)
        else:
            print("This password has already been used!")


if __name__ == "__main__":
    alexi = PasswordManager()
    alexi.set_password("Heyhoi")
    alexi.get_password()
    alexi.set_password("Heyhoi")
    alexi.is_correct("bonkers")
