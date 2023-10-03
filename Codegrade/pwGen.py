from random import randint


def generate_random_password():
    passwd = ""
    pwLength = randint(7, 10)
    for character in range(pwLength):
        asciiChar = chr(randint(33, 126))
        passwd += asciiChar
    print(passwd)


if __name__ == "__main__":
    generate_random_password()