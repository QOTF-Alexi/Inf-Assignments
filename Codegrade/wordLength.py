from sys import argv


file = argv[-1]


# Find maximum word length
def maxWordLength(inFile):
    maxLength = 0
    with open(inFile) as data:
        for line in data:
            for word in line.split():
                wordLength = len(word)
                if wordLength > maxLength:
                    maxLength = wordLength
    return maxLength


# Return words with max length
def longestWords(maxLength, inFile):
    wordList = []
    with open(inFile) as data:
        for line in data:
            for word in line.split():
                if len(word) == maxLength:
                    wordList.append(word)
    return wordList


if __name__ == "__main__":
    file = input("Which file should be used? ")
    try:
        maxLength = maxWordLength(file)
        wordList = longestWords(maxLength, file)
        print(f"Length of longest words is [{maxLength}] chars")
        print("These are all the words of that length:")
        print(*wordList)
    except FileNotFoundError:
        print("Error reading file,", file)