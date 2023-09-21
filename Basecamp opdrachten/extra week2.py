def divtest():
    readNum = int(input("Enter a number: "))
    if readNum % 5 == 0:
        print(":)")
    else:
        print(":(")

def twodigit():
    tdin = int(input("Enter a number: "))
    if tdin >= 10:
        print("TRUE")
    else:
        print("FALSE")

def divbyzero():
    divA = int(input("Enter a value for A: "))
    divB = int(input("Enter a value for B: "))
    if divB == 0:
        print("Cannot divide by zero")
    else:
        divC = divA/divB
        print(divC)

def sumEven():
    sumA = int(input("Enter a value for A: "))
    sumB = int(input("Enter a value for B: "))
    sumC = int(input("Enter a value for C: "))
    sumList = [sumA, sumB, sumC]
    res = sum(i for i in sumList if i % 2 == 0)
    print(res)

def analyseLessons():
    day = int(input("Enter a day between 1-12: "))
    week = 1
    if day > 12:
        print("Invalid date")
    else: 
        if day % 2 != 0:
            lessonType = 'theoretical'
        else:
            lessonType = 'practical'
        # To be finished

def bonusCalculator():
    salary = int(input("Enter the employee's annual salary: "))
    if salary < 30000:
        print("Bonus:", (salary*0.10))
    elif 30000 <= salary < 40000:
        print("Bonus:", (salary*0.12))
    elif 40000 <= salary < 55000:
        print("Bonus:", (salary*0.14))
    else:
        print("Bonus:", (salary*0.15))

def greenLantern():
    gender = input("Enter the gender as m/f: ")
    age = int(input("Enter the age: "))
    if gender == 'm' and age <= 40:
        weight = int(input("Enter the weight: "))
        if weight <= 80:
            print("Recruit.")
        else:
            print("Do not recruit.")
    elif gender == 'f' and age >= 20:
        height = int(input("Enter the height: "))
        if height >= 160:
            print("Recruit.")
        else:
            print("Do not recruit.")
    else:
        print("Do not recruit.")



greenLantern()