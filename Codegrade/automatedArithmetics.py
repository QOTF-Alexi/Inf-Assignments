from random import randint

generate_exercises = 10
typeGiven = False

while typeGiven == False:
    arithmetic_type = str(input("Enter the arithmetic type (summation, multiplication, subtraction): "))
    if arithmetic_type == "summation" or arithmetic_type == "multiplication" or arithmetic_type == "subtraction":
        typeGiven = True
    else:
        print("That is not a valid type!")
        typeGiven = False


def arithmetic_operation(arithmetic_type):
    correct = 0
    incorrect = 0
    operationDict = {
        "summation": '+',
        "multiplication": '*',
        "subtraction": '-'
    }
    print("Arithmetic operation:", arithmetic_type)
    for i in range(generate_exercises):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operation = operationDict[arithmetic_type]
        print(num1, operation, num2, "=", end='')
        userAns = int(input(" "))
        if operation == '+':
            correctAns = num1+num2
        elif operation == '*':
            correctAns = num1*num2
        elif operation == '-':
            correctAns = num1-num2
        else:
            print("How did I get here?")
        if correctAns == userAns:
            correct += 1
        else:
            incorrect += 1
    print("You got", correct, "correct and", incorrect, "incorrect answers in", arithmetic_type)


if __name__ == "__main__": # Only runs the function if the file is accessed directly.
    arithmetic_operation(arithmetic_type)