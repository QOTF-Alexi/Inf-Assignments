global key
global keydict


def set_dict_key(key: str):
    dict_key = {}
    if (len(key)/2) % 2 == 0:
        for char in range((len(key) // 2)):
            dict_key |= {key[2 * char]: key[1 + 2 * char]}
        return dict_key
    else:
        print("Invalid hashvalue input")
        return None


def encode_function(data: str):
    global keydict
    encodedStr = ""
    for char in data:
        encodedStr += keydict[char]


def decode_function(data: str):
    global keydict
    inverse_keydict = {value: key for key, value in keydict.items()}
    decodedStr = ""
    for char in data:
        decodedStr += inverse_keydict[char]


def encode_string(data: str, hofunction) -> str:
    return hofunction(data)


def decode_string(data: str, hofunction) -> str:
    return hofunction(data)


def encode_list(data: list, key) -> list:
    global keydict
    keydict = set_dict_key(key)
    encodedList = []
    for element in data:
        encodedElement = encode_string(element, encode_function)
        encodedList.append(encodedElement)
    return encodedList


def decode_list(data: list, key) -> list:
    global keydict
    keydict = set_dict_key(key)
    decodedList = []
    for element in data:
        decodedElement = decode_string(element, decode_function)
        decodedList.append(decodedElement)
    return decodedList


def validate_values(encoded: str, decoded: str, key) -> bool:
    global keydict
    keydict = set_dict_key(key)
    if ', ' in encoded:
        decodeStr = decode_list(encoded.split(sep=", "), key)
    else:
        decodeStr = decode_string(encoded, encode_function)

    if ', ' in decoded:
        encodeStr = encode_list(decoded.split(sep=", "), key)
    else:
        encodeStr = encode_string(decoded, decode_function)

    if decodeStr == decoded and encodeStr == encoded:
        return True
    else:
        return False


def main():
    global key
    global keydict
    running = True
    encoded_values = []
    decoded_values = []
    while running:
        print("[E] Encode value to hashed value")
        print("[D] Decode hashed value to normal value")
        print("[P] Print all encoded/decoded values")
        print("[V] Validate 2 values against eachother")
        print("[Q] Quit program")
        key = input("Key: ")
        if key.upper() == "Q":
            break
        else:
            keydict = set_dict_key(key)
        menuChoice = (input("What would you like to do? ")).upper()
        if menuChoice == "E":
            toHash = input("Enter a normal string: ")
            if ', ' in toHash:
                encoded_values += encode_list(toHash.split(sep=", "), key)
            else:
                encoded_values.append(encode_string(toHash, encode_function))
        elif menuChoice == "D":
            toString = input("Enter a hashed string: ")
            if ', ' in toString:
                decoded_values += decode_list(toString.split(sep=", "), key)
            else:
                decoded_values.append(decode_string(toString, decode_function))
        elif menuChoice == "P":
            print(*encoded_values, sep="\n")
            print(*decoded_values, sep="\n")
        elif menuChoice == "V":
            hashStr = input("Enter a hashed string: ")
            normalStr = input("Enter a normal string: ")
            if validate_values(hashStr, normalStr, key):
                print("These strings match!")
            else:
                print("These strings do not match!")
        elif menuChoice == "Q":
            running = False


# Create a unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    main()