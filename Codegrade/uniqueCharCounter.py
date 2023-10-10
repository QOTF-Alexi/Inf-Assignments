def unique_chars_dict(testString):
    testDict = {}

    for char in testString:
        testDict[char] = testDict.get(char, 0) + 1
    uniqueCharsNum = len(testDict)
    print("Unique characters:", uniqueCharsNum)


def unique_chars_set(testString):
    testSet = set(testString)
    uniqueCharsNum = len(testSet)
    print("Unique characters:", uniqueCharsNum)


if __name__ == "__main__":
    testString = input("Enter a string: ")
    unique_chars_dict(testString)
    unique_chars_set(testString)
