# Galgje v2, door B.M. Prins

from os import system, name
from time import sleep

def clrscr(): # Uitgaande dat dit uit terminal wordt gespeeld
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
def display_word(word, guesses):
    # Geeft een string met underscores voor te raden letters, en de letter wanneer die geraden is.
    result = ""
    for letter in word:
        if letter in guesses:
            result += letter
        else:
            result += "_"
    return result

def hangman():
    word = input("Enter the word to be guessed: ") # Vraagt gebruiker 1 voor een woord
    correct_guesses = set()  # Slaat juist geraden letters op in set
    incorrect_guesses = set()  # Slaat onjuist geraden letters op in set
    num_guesses = 8  # Aantal toegestane onjuiste gokken

    clrscr()
    print("Galgje!")
    print()
    print("Het woord bevat", len(word), "letters.")
    print(display_word(word, correct_guesses))

    while True:
        guess = input("Gok een letter: ")
        if guess in correct_guesses or guess in incorrect_guesses:
            print("Die letter is al gegeven!")
        elif len(guess) > 1:
            print("Dat is meer dan 1 letter")
        elif guess in word:
            correct_guesses.add(guess)
            print(display_word(word, correct_guesses))
            if set(word) == correct_guesses:
                print("Gefeliciteerd, je hebt gewonnen!")
                break
        else:
            incorrect_guesses.add(guess)
            num_guesses -= 1
            print("Onjuist!")
            print(f"Je hebt {num_guesses} gokken over.")
            if num_guesses == 0:
                print("Sorry, je hebt verloren!")
                print(f"Het woord was {word}.")
                break

hangman()
sleep(5) # Geeft 5 seconden timeout in terminal, zodat de gebruiker het eindresultaat kan zien.
