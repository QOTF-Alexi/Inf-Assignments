import os
import sys
import json


def read_from_json(filename) -> list:
    collection = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        json_data = json.load(outfile)
        # iterate over each line in data and call the add function
        for movie in json_data:
            collection.append(movie)

    return collection


def write_to_json(filename, collection: list) -> None:
    json_object = json.dumps(collection, indent=4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


def infos(data):
    yearNum = 0
    sfNum = 0
    reevesList = []
    stalloneList = []
    for movie in data:
        if movie["year"] == 2004:
            yearNum += 1
        if "Science Fiction" in movie["genres"]:
            sfNum += 1
        if "Keanu Reeves" in movie["cast"]:
            reevesList.append(movie)
        if "Sylvester Stallone" in movie["cast"] and 1995 <= movie["year"] <= 2005:
            stalloneList.append(movie)
    print(f"{yearNum}\n{sfNum}")
    print(*reevesList, "\n", *stalloneList)


def modify(data):
    releaseYear = 2023
    for movie in data:
        if movie["title"] == "Gladiator":
            movie["year"] = 2001
        if "Natalie Portman" in movie["cast"]:
            movie["cast"].remove("Natalie Portman")
            movie["cast"].append("Nat Portman")
        if "Kevin Spacey" in movie["cast"]:
            movie["cast"].remove("Kevin Spacey")
        if movie["year"] < releaseYear:
            releaseYear = movie["year"]
    for movie in data:
        if movie["year"] == releaseYear:
            movie["year"] -= 1
    return data


def searchTitle(data):
    searchList = []
    criterium = input("Enter a title: ")
    for movie in data:
        if criterium in movie["title"]:
            searchList.append(movie)
    return searchList


def changeTitleOrYear(data):
    criterium = input("Enter a title: ")
    newTitle = str(input("Enter a new title: "))
    newYear = int(input("Enter a new year: "))
    for movie in data:
        if criterium in movie["title"]:
            movie["title"] = newTitle
            movie["year"] = newYear


def main() -> None:
    json_file = "movies.json"
    collection = read_from_json(json_file)
    running = True
    while running:
        print("[I] Movie information overview")
        print("[M] Make modification based on assignment")
        print("[S] Search a movie title ")
        print("[C] Change title and/or release year by search on title")
        print("[Q] Quit program")

        menuChoice = input("What would you like to do? ").upper()
        if menuChoice == "I":
            infos(collection)
        elif menuChoice == "M":
            modify(collection)
            write_to_json(json_file, collection)
        elif menuChoice == "S":
            print(*searchTitle(collection))
        elif menuChoice == "C":
            changeTitleOrYear(collection)
            write_to_json(json_file, collection)
        elif menuChoice == "Q":
            running = False
        else:
            print("That's not a valid entry!")


if __name__ == "__main__":
    main()