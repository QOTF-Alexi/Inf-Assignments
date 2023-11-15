from sys import argv


file = argv[-1]


# Find most found word
def maxWordAmount(inFile):
    maxAmount = 0
    maxAmountList = {}
    currentAmount = 0
    currentWord = ""
    with open(inFile) as data:
        for line in data:
            for currentWord in line.split():
                # Next line makes word lowercase and removes punctuation.
                currentWord = (currentWord.lower()).strip(",.;:'\"?!&()")
                for word in line.split():
                    word = (word.lower()).strip(",.;:'\"?!&()")
                    if currentWord == word:
                        currentAmount += 1
                    else:
                        pass
                if currentAmount > maxAmount:
                    maxAmount = currentAmount
                    maxAmountList = {currentWord}
                elif currentAmount == maxAmount:
                    maxAmountList += {currentWord}
                else:
                    pass
    return maxAmountList


# Return words that appear least
def minWordAmount(inFile):
    minAmount = float('inf')
    minAmountList = {}
    currentAmount = 0
    currentWord = ""
    with open(inFile) as data:
        for line in data:
            for currentWord in line.split():
                currentWord = (currentWord.lower()).strip(",.;:'\"?!&()")
                for word in line.split():
                    word = (word.lower()).strip(",.;:'\"?!&()")
                    if currentWord == word:
                        currentAmount += 1
                    else:
                        pass
                if currentAmount < minAmount:
                    minAmount = currentAmount
                    minAmountList = {currentWord}
                elif currentAmount == minAmount:
                    minAmountList += {currentWord}
                else:
                    pass
    return minAmountList


if __name__ == "__main__":
    file = input("Which file should be used? ")
    try:
        maxWords = maxWordAmount(file)
        minWords = minWordAmount(file)
        print(f"Most: {list(maxWords)}")
        print(f"Least: {list(minWords)}")
    except FileNotFoundError:
        print("Error reading file,", file)