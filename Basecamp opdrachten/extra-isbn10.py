def validateCompleteNum(isbn):
        if isbn[9] == 'X':
            check = 10
        else:
            check = int(isbn[9])
        multi = 10
        n = 0
        control = 0
        for i in range (9):
            control += int(isbn[n]) * multi
            n += 1
            multi -= 1
        if 11-(control % 11) == check:
            print("VALID")
        else:
            print("INVALID")


def calculateMissing(isbn):
    if '.' in isbn:
        dotindex = isbn.find('.')
        multi = 10
        control = 0
        for n in isbn:
            if n == '.':
                n = 0
            control += int(n) * multi
            multi -= 1

        multi = 10
        for i in range(11):
            factor = multi - dotindex
            if (control + factor * i) % 11 == 0:
                if i == 10:
                    i = 'X'
                print(i)

isbn = input("Enter an ISBN: ")
if len(isbn) == 10:
    if isbn.count('.') == 0:
        validateCompleteNum(isbn)
    elif isbn.count('.') == 1:
        calculateMissing(isbn)
else:
    print("INPUT ERROR")