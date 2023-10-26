def encode_string(data: str, key: str = None) -> str:
    keydict = set_dict_key(key)
    encodedStr = str()
    for char in data:
        encodedStr += keydict[char]
    return encodedStr


def decode_string(data: str, key: str = None) -> str:
    keydict = set_dict_key(key)
    inverse_keydict = {value: key for key, value in keydict.items()}
    decodedStr = str()
    for char in data:
        decodedStr += inverse_keydict[char]
    return decodedStr


def encode_list(data: list, key: str = None) -> list:
    encodedList = []
    for element in data:
        encodedElement = encode_string(element, key)
        encodedList.append(encodedElement)
    return encodedList


def decode_list(data: list, key: str = None) -> list:
    decodedList = []
    for element in data:
        decodedElement = decode_string(element, key)
        decodedList.append(decodedElement)
    return decodedList


def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    if ', ' in encoded:
        decodeStr = decode_list(encoded.split(sep=", "), key)
    else:
        decodeStr = decode_string(encoded, key)

    if ', ' in decoded:
        encodeStr = encode_list(decoded.split(sep=", "), key)
    else:
        encodeStr = encode_string(decoded, key)

    if decodeStr == decoded and encodeStr == encoded:
        return True
    else:
        return False


def set_dict_key(key: str) -> None:
    dict_key = {}
    if (len(key)/2) % 2 == 0:
        for char in range((len(key) // 2)):
            dict_key |= {key[2 * char]: key[1 + 2 * char]}
        return dict_key
    else:
        print("Invalid hashvalue input")
        return False


def main():
    key = input("Key: ")
    running = True
    keydict = set_dict_key(key)   # Check if valid, crash otherwise
    if not keydict:
        running = False
    encoded_values = []
    decoded_values = []
    while running:
        print("[E] Encode value to hashed value")
        print("[D] Decode hashed value to normal value")
        print("[P] Print all encoded/decoded values")
        print("[V] Validate 2 values against eachother")
        print("[Q] Quit program")
        menuChoice = (input("What would you like to do? ")).upper()
        if menuChoice == "E":
            toHash = input("Enter a normal string: ")
            if ', ' in toHash:
                encoded_values += encode_list(toHash.split(sep=", "), key)
            else:
                encoded_values.append(encode_string(toHash, key))
        elif menuChoice == "D":
            toString = input("Enter a hashed string: ")
            if ', ' in toString:
                decoded_values += decode_list(toString.split(sep=", "), key)
            else:
                decoded_values.append(decode_string(toString, key))
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