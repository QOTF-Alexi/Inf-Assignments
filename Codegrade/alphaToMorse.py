morse_dict = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', ' ': '  ', '': ''}


def message_to_morse(message):
    message = message.upper()
    cipher = ''
    for letter in message:
        if letter not in morse_dict:
            cipher = letter
            break
        else:
            cipher += morse_dict[letter] + ' '
    if len(cipher) > 1:
        print(cipher)
    else:
        print(f"Can\'t convert char [{cipher}]")


def morse_to_message(message):
    message += ' '
    decipher = ''
    citext = ''

    for letter in message:
        if (letter != ' '):
            indicator = 0
            citext += letter
        else:
            indicator += 1

            if indicator == 2:
                decipher += ' '
            else:
                decipher += list(morse_dict.keys())[list(morse_dict.values()).index(citext)]
                citext = ''
    print(decipher)


# Lazy method to determine message type. Never use this in production
def translate_text(message):
    if message.startswith(".") or message.startswith("-"):
        morse_to_message(message)
    else:
        message_to_morse(message)


if __name__ == "__main__":
    messageInput = input("Enter a string: ")
    translate_text(messageInput)