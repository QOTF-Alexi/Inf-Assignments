from random import randint

generate_exercises_amount = 10
typeGiven = False

while typeGiven is False:
    arithmetic_type = str(input("Enter the arithmetic type (summation, multiplication, subtraction): "))
    if arithmetic_type == "summation" or arithmetic_type == "multiplication" or arithmetic_type == "subtraction":
        typeGiven = True
    else:
        print("That is not a valid type!")
        typeGiven = False


def generateProblem(arithmetic_type):
    operationDict = {
        "summation": '+',
        "multiplication": '*',
        "subtraction": '-'
    }

    exerciseSummand1 = randint(1, 100)
    exerciseSummand2 = randint(1, 100)
    operation = operationDict[arithmetic_type]

    if operation == '+':
        correctAns = exerciseSummand1+exerciseSummand2
    elif operation == '*':
        correctAns = exerciseSummand1*exerciseSummand2
    elif operation == '-':
        correctAns = exerciseSummand1-exerciseSummand2
    else:
        print("How did I get here?")
    print(exerciseSummand1, operation, exerciseSummand2, "=", end='')
    return correctAns


def arithmetic_operation(arithmetic_type):
    correct = 0
    incorrect = 0
    print("Arithmetic operation:", arithmetic_type)
    for exercise in range(generate_exercises_amount):
        correctAns = generateProblem(arithmetic_type)
        intGiven = False
        while not intGiven:
            try:
                userAns = int(input(" "))
                if correctAns == userAns:
                    correct += 1
                else:
                    incorrect += 1
                intGiven = True
            except ValueError:
                print("That is not a number!")
    print("You got", correct, "correct and", incorrect, "incorrect answers in", arithmetic_type)


if __name__ == "__main__":      # Only runs the function if the file is accessed directly.
    arithmetic_operation(arithmetic_type)