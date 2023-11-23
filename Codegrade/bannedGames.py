import os
import sys
import csv


def load_csv_file(file_name):
    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))

    return file_content


# Should completely overwrite the file.
def write_csv_file(file_name, data):
    with open(os.path.join(sys.path[0], file_name), 'w', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def assignmentModify(dataset):
    iteration = 0
    # Don't ask why, but it needs to be run twice
    while iteration != 2:
        for entry in dataset:
            if entry[3] == "Germany":
                dataset.remove(entry)
            elif "Silent Hill VI" in entry[1]:
                entry[1] = "Silent Hill Remastered"
            elif entry[1] == "Bully" and entry[3] == "Brazil":
                entry[6] = "Ban Lifted"
            elif entry[1] == "Manhunt II" and entry[12] == "Stealth":
                entry[12] = "Action"
        iteration += 1
    return dataset


def addNewGame(dataset):
    ident = input("Enter a unique ID: ")
    name = input("Enter a name: ")
    series = input("Enter a series: ")
    country = input("Enter a country: ")
    details = input("Enter any details: ")
    category = input("Enter a category: ")
    status = input("Enter the current status: ")
    wikipedia = input("Enter a Wikipedia article: ")
    image = input("Enter an image: ")
    summary = input("Enter a summary: ")
    developer = input("Enter the developer: ")
    publisher = input("Enter the publisher: ")
    genre = input("Enter the genre: ")
    homepage = input("Enter a homepage: ")
    dataset.append([ident, name, series, country, details, category, status, wikipedia, image,
                   summary, developer, publisher, genre, homepage])
    return dataset


def overviewPerCountry(dataset):
    countries = []
    overviewDict = {}
    for entry in dataset:
        countries.append(entry[3])
    countries.remove("Country")
    countriesSet = set(countries)
    countries = sorted(list(countriesSet))

    for country in countries:
        banList = []
        for entry in dataset:
            if country in entry:
                banList.append(entry[1])
        overviewDict[country] = banList

    return overviewDict


def searchByCountry(dataset, criterium):
    bannedInCountry = []
    for entry in dataset:
        if criterium in entry:
            bannedInCountry.append(f"{entry[1]} - {entry[4]}")
    return bannedInCountry


# INCOMPLETE FUNCTION
def assignmentInfo(dataset):
    bannedisrael = len(searchByCountry(dataset, "Israel"))
    print(bannedisrael)

    maxBans = 0
    banDict = overviewPerCountry(dataset)
    for country in banDict:
        bans = banDict[country]
        if maxBans < len(bans):
            maxBans = len(bans)
    for country in banDict:
        bans = banDict[country]
        if maxBans == len(bans):
            print(country)

    for entry in dataset:
        acBan = []
        if entry[2] == "Assassin's Creed":
            acBan.append(entry)
    print(len(set(acBan)))

    germanBans = searchByCountry(dataset, "Germany")
    print(*germanBans, sep="\n")

    rddBan = []
    for entry in dataset:
        if entry[1] == "Red Dead Redemption":
            rddBan.append(f"{entry[3]} - {entry[4]}")
    print(*rddBan, sep="\n")


def main(filename: str) -> None:
    dataset = load_csv_file(filename)
    running = True
    while running:
        print("[I] Print request info from assignment")
        print("[M] Make modification based on assignment")
        print("[A] Add new game to list")
        print("[O] Overview of banned games per country")
        print("[S] Search the dataset by country")
        print("[Q] Quit program")

        menuChoice = input("What would you like to do? ").upper()
        if menuChoice == "I":
            assignmentInfo(dataset)
        elif menuChoice == "M":
            dataset = assignmentModify(dataset)
            write_csv_file(filename, dataset)
        elif menuChoice == "A":
            dataset = addNewGame(dataset)
            write_csv_file(filename, dataset)
        elif menuChoice == "O":
            overviewDict = overviewPerCountry(dataset)
            for country in overviewDict:
                print("\n")
                print(f"{country} - {len(overviewDict[country])}")
                for element in overviewDict[country]:
                    print("-", element)
        elif menuChoice == "S":
            criterium = input("Enter a country: ")
            print(*searchByCountry(dataset, criterium))
        elif menuChoice == "Q":
            running = False
        else:
            print("That is not a valid entry!")


if __name__ == "__main__":
    main("bannedvideogames.csv")