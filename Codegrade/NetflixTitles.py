import os
import sys
import csv


def load_csv_file(file_name):
    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))

    return file_content


def get_headers(file_content):
    return file_content[0]


def get_directors(file_content):
    directors = []
    for row in file_content:  # iteration makes it work, not sure why
        if row[3] != '' and row[3] != 'director':
            directors.append(row[3])
    return directors


def checkTVShows(data):
    tvShows = 0
    for element in data:
        if element[1] == "TV Show":
            tvShows += 1
    return tvShows


def checkMovies(data):
    movies = 0
    for element in data:
        if element[1] == "Movie":
            movies += 1
    return movies


def search_by_type(file_content, show_type):
    ()


def search_by_director(file_content, director):
    recordings = []
    for element in file_content:  # iteration makes it work, not sure why
        if director == element[3]:
            recordings.append(element[2])
    return recordings


def has_directed_both(data):
    directors = set(get_directors(data))
    directedBoth = []
    for director in directors:
        directedShow = False
        directedMovie = False
        for element in data:
            if element[3] == director:
                if element[1] == "TV Show":
                    directedShow = True
                elif element[1] == "Movie":
                    directedMovie = True
        if directedShow and directedMovie:
            directedBoth.append(director)
    return directedBoth


def print_all(data):
    ()


def main(filename):
    file = load_csv_file(filename)
    print("[1] Print the amount of TV Shows")
    print("[2] Print the amount of Movies")
    print("[3] Print the (full) names of directors in alphabetical order who lead both tv shows and movies.")
    print("[4] Print the name of each director in alphabetical order and ", end="")
    print("the number of movies and the number of tv shows they were the director of.")
    menuChoice = str(input("What would you like to do? "))
    if menuChoice == "1":
        print("There are", checkTVShows(file), "TV Shows in the database.")
    elif menuChoice == "2":
        print("There are", checkMovies(file), "Movies in the database.")
    elif menuChoice == "3":
        print(*(has_directed_both(file)), sep=", ")
    elif menuChoice == "4":
        ()
    elif menuChoice == "5":
        print(*(search_by_director(file, "Steven Spielberg")), sep=", ")
    else:
        print("That is not a valid entry!")


if __name__ == "__main__":
    username = os.getenv("USERNAME")
    if username == 'benno':
        main("netflix_titles_ingekort.csv")
    else:
        main("netflix_titles.csv")