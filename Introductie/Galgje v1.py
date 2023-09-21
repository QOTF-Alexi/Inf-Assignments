# Versie 1 door B.M. Prins
print('G A L G J E')
print()
word = input('Geef een woord om te laten raden: ')

playing = True
guessedLetters = 0
missedLetters = 0
secretWord = []

for y in word:
    secretWord += "_"

while playing:
    letterInWord = False
    print(secretWord)
    letter = input('Vul een letter in: ')
    for x in range(len(word)):
        if letter == word[x]:
            secretWord[x] = letter
            letterInWord = True
            guessedLetters += 1
        elif letterInWord == False:
            missedLetters += 1
            print('Helaas is dat niet goed. Je hebt ', str(missedLetters), 'fouten. Je mag maximaal 8 fouten hebben.')
        elif guessedLetters == len(word):
            print('Yay, je hebt gewonnen! Het woord was ', word)
            playing = False
        elif missedLetters >= 8:
            print('Game over, te veel fout. Het woord was ', word)
            playing = False
                
