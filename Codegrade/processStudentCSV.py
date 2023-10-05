import os
import sys

valid_lines = []
corrupt_lines = []
invalid_data = []

illegalChars = "1234567890,./<>?`~!@#$%^&*()_+=[]{}|;:\'\""
validProgrammes = ["INF", "TINF", "CMD", "AI"]


def validate_data(line):
    invalid_data = []
    splitLine = line.split(sep=",")
    studNum = str(splitLine[0])
    firstName = str(splitLine[1])
    lastName = str(splitLine[2])

    birthDate = (str(splitLine[3])).split(sep="-")
    birthYear = int(birthDate[0])
    birthMonth = int(birthDate[1])
    birthDay = int(birthDate[2])

    studProgramme = str(splitLine[4])

    if studNum.startswith("08") or line.startswith("09"):
        studNumValid = True
    else:
        studNumValid = False
        invalid_data.append(studNum)

    if not any(element in firstName for element in illegalChars):
        firstNameValid = True
    else:
        firstNameValid = False
        invalid_data.append(firstName)

    if not any(element in lastName for element in illegalChars):
        lastNameValid = True
    else:
        lastNameValid = False
        invalid_data.append(lastName)

    if studProgramme in validProgrammes:
        studProgrammeValid = True
    else:
        studProgrammeValid = False
        invalid_data.append(studProgramme)

    if 1960 <= birthYear <= 2004:
        birthYearValid = True
    else:
        birthYearValid = False

    if 1 <= birthMonth <= 12:
        birthMonthValid = True
    else:
        birthMonthValid = False

    if 1 <= birthDay <= 31:
        birthDayValid = True
    else:
        birthDayValid = False

    if birthYearValid and birthMonthValid and birthDayValid:
        birthDateValid = True
    else:
        birthDateValid = False
        invalid_data.append(splitLine[3])

    if studNumValid and firstNameValid and lastNameValid and studProgrammeValid and birthDateValid:
        valid_lines.append(",".join(str(element) for element in splitLine))
    else:
        corrupt_lines.append(str(",".join(str(element) for element in splitLine)) +
                             " => INVALID DATA: " + str(invalid_data))


def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        # skip header line
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())

    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":
    main('students.csv')
