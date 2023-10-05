gifts = [
    "partridge in a pear tree", "turtledoves", "french hens",
    "calling birds", "gold rings (five golden rings)", "geese a-laying",
    "swans a-swimming", "maids a-milking", "ladies dancing",
    "lords a-leaping", "pipers piping", "drummers drumming"
]

numberToText = {
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve"
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

    verse = verse + " day of Christmas, my true love sent to me"
    for giftNumber in range(day - 1, -1, -1):  # Loops through the list of gifts, in reverse order
        if giftNumber == 0:
            if day == 1:
                verse += " A " + gifts[giftNumber]
            else:
                verse = verse[:-1]  # remove the last comma
                verse += " And A " + gifts[giftNumber]
        else:
            verse += " " + numberToText[(giftNumber + 1)] + " " + gifts[giftNumber] + ","
    print(verse + "\n")


if __name__ == "__main__":
    for complete in range(1, 13):
        next_verse(complete)
