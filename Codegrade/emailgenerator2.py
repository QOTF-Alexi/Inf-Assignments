def mainloop():
    while True:
        moreLetters = input("More letters? (Yes or No) ")
        if moreLetters == "Yes":
            while True:
                letterType = input("Job Offer or Rejection? ")
                if letterType == "Rejection" or letterType == "Job Offer":
                    basicInfo(letterType)
                    break
                else:
                    print("Input error")
        elif moreLetters == "No":
            exit()
        else:
            print("Input error")


def basicInfo(letterType):
    while True:
        firstName = input("First name? ")
        if (firstName[0].isupper() and len(firstName) >= 2 and len(firstName) <= 10):
            break
        else:
            print("Input Error")
    while True:
        lastName = input("Last name? ")
        if (lastName[0].isupper() and len(lastName) >= 2 and len(lastName) <= 10):
            break
        else:
            print("Input error")
    while True:
        jobTitle = input("Job title? ")
        if (len(jobTitle) >= 10 and not any(char.isdigit() for char in jobTitle)):
            break
        else:
            print("Input error")
    if letterType == 'Job Offer':
        offerInfo(firstName, lastName, jobTitle)
    elif letterType == 'Rejection':
        rejectInfo(firstName, lastName, jobTitle)


def offerInfo(firstName, lastName, jobTitle):
    while True:
        annualSalary = (input("Annual Salary? "))
        if (annualSalary[2] != "." or annualSalary[6] != "," or not 1 < int(annualSalary[0]) < 8):
            print("Input error")
        else:
            break
    while True:
        startingDate = input("Start Date? (YYYY-MM-DD) ")
        startingDate = startingDate.split(sep='-')
        if 1 <= int(startingDate[2]) <= 31 and 1 <= int(startingDate[1]) <= 12 and 2021 <= int(startingDate[0]) <= 2022:
            break
        else:
            print("Input error")
    print("Here is the final letter to send:")
    print(f"Dear {firstName} {lastName}, ")
    print(f" After careful evaluation of your application for the position of {jobTitle}, ")
    print(f" we are glad to offer you the job. Your salary will be {annualSalary} euro annually. ")
    print(f"Your start date will be on {startingDate[0]}-{startingDate[1]}-{startingDate[2]}.")
    print("Please do not hesitate to contact us with any questions. ")
    print("Sincerely, \nHR Department of XYZ ")


def rejectInfo(firstName, lastName, jobTitle):
    giveFeedback = input("Feedback? (Yes or No) ")
    if giveFeedback == 'Yes':
        feedbackStatement = input("Enter your Feedback (One Statement): ")
    elif giveFeedback == 'No':
        ()
    else:
        print("Input error")
    print("Here is the final letter to send:")
    print(f"Dear {firstName} {lastName}, ")
    print(f"After careful evaluation of your application for the position of {jobTitle}, ")
    print("at this moment we have decided to proceed with another candidate. ")
    if giveFeedback == 'Yes':
        print("Here we would like to provide you our feedback about the interview.")
        print(feedbackStatement)
    print("We wish you the best in finding your future desired career.")
    print("Please do not hesitate to contact us with any questions. \nSincerely, HR Department of XYZ ")


mainloop()