import os
import sys

valid_lines = []
corrupt_lines = []

'''
The validate_data function will check the students.csv line by line for corrupt data.

- Valid lines should be added to the valid_lines list.
- Invalid lines should be added to the corrupt_lines list.

Example input: 0896801,Kari,Wilmore,1970-06-18,INF
This data is valid and the line should be added to the valid_lines list unchanged.

Example input: 0773226,Junette,Gur_ry,1995-12-05,
This data is invalid and the line should be added to the corrupt_lines list in the following format:

0773226,Junette,Gur_ry,1995-12-05, => INVALID DATA: ['0773226', 'Gur_ry', '']

In the above example the studentnumber does not start with '08' or '09',
the last name contains a special character and the student program is empty.

Don't forget to put the students.csv file in the same location as this file!
'''

illegalChars = "1234567890,./<>?`~!@#$%^&*()_+=[]{}|;:\'\""
validProgrammes = ["INF", "TINF", "CMD", "AI"]


def validate_data(line):
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

    if not any(element in firstName for element in illegalChars):
        if not any(element in lastName for element in illegalChars):
            nameValid = True
        else:
            nameValid = False
    else:
        nameValid = False

    if studProgramme in validProgrammes:
        studProgrammeValid = True
    else:
        studProgrammeValid = False

    if 1960 <= birthYear <= 2004:
        if 1 <= birthMonth <= 12:
            if 1 <= birthDay <= 31:
                birthDateValid = True
            else:
                birthDateValid = False
        else:
            birthDateValid = False
    else:
        birthDateValid = False

    if studNumValid and nameValid and studProgrammeValid and birthDateValid:
        valid_lines.append(",".join(str(element) for element in splitLine))
    else:
        corrupt_lines.append(",".join(str(element) for element in splitLine))


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