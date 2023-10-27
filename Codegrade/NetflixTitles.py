import os
import sys
import csv


# Provided code for loading the CSV file
def load_csv_file(file_name):
    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))

    return file_content


# Fetches the headers of the provided file
def get_headers(file_content):
    return file_content[0]


# Fetches all the (entered) directors inside the provided file
def get_directors(file_content):
    directors = []
    for row in file_content:
        if row[3] != '' and row[3] != 'director':
            directors.append(row[3])
    return directors


# Calculates the number of TV shows in the database
def checkTVShows(data):
    tvShows = 0
    for element in data:
        if element[1] == "TV Show":
            tvShows += 1
    return tvShows


# Calculates the number of Movies in the database
def checkMovies(data):
    movies = 0
    for element in data:
        if element[1] == "Movie":
            movies += 1
    return movies


# Function that returns every recording based on the type
def search_by_type(file_content, show_type):
    recordings = []
    for element in file_content:
        if show_type == element[1]:
            recordings.append(element[2])
    return recordings


# Function that returns every recording based on the director
def search_by_director(file_content, director):
    recordings = []
    for element in file_content:
        if director == element[3]:
            recordings.append(element[2])
    return recordings


# Calculates the number of TV shows and Movies a director has directed
def director_lead_num(data):
    directors = set(get_directors(data))
    directors_count = []
    for director in directors:
        tvShows = 0
        movies = 0
        # Iterate through the entire list, both types separately
        for element in data:
            if element[3] == director:
                if element[1] == "TV Show":
                    tvShows += 1
        for element in data:
            if element[3] == director:
                if element[1] == "Movie":
                    movies += 1
        directors_count.append((director, movies, tvShows))
    return sorted(directors_count)


# Checks if a director has directed both TV Shows and Movies
def has_directed_both(data):
    directors_count = director_lead_num(data)
    directed_both = []
    for element in directors_count:
        if element[1] > 0 and element[2] > 0:
            directed_both.append(element[0])
    return directed_both


# Main function to provide menu structure
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
        print(has_directed_both(file))
    elif menuChoice == "4":
        print(director_lead_num(file))
    else:
        print("That is not a valid entry!")


if __name__ == "__main__":
    username = os.getenv("USERNAME")            # Fetches username of the OS
    if username == 'benno':                     # Use different file for my username
        main("netflix_titles_ingekort.csv")
    else:                                       # Use default file for CodeGrade
        main("netflix_titles.csv")