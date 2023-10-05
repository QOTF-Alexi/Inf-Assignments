gifts = [
    'partridge in a pear tree', 'pipers piping', 'lords a-leaping',
    'ladies dancing', 'maids a-milking', 'swans a-swimming',
    'geese a-laying', 'gold rings', 'calling birds', 'French hens',
    'turtle doves', 'drummers drumming'
]

numberToText = {
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve"
}


def next_verse(vers_number):
    for day in range(1, vers_number + 1):
        if day == 1:
            verse = "On the " + str(day) + "st"
        elif day == 2:
            verse = "On the " + str(day) + "nd"
        elif day == 3:
            verse = "On the " + str(day) + "rd"
        else:
            verse = "On the " + str(day) + "th"

    verse = verse + " day of Christmas my true love sent to me"
    for giftNumber in range(day - 1 , -1, -1):  #Loops through the list of gifts, in reverse order
        if giftNumber == 0:
            if day == 1:
                verse += " a " + gifts[giftNumber] + "."
            else:
                verse = verse[:-1]  # remove the last comma
                verse += " and a " + gifts[giftNumber] + "."
        else:
            verse += " " + numberToText[(giftNumber + 1)] + " " + gifts[giftNumber] + ","
    print(verse +"\n")


if __name__ == "__main__":
    vers_number = 3
    next_verse(vers_number)
