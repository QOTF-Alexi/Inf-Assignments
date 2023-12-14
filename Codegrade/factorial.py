def factorial(n):
    # initialize the result to 1
    result = 1
    # loop from 1 to n
    for i in range(1, n+1):
        # multiply the result by i
        result = result * i
    # return the result
    return result


def rec_factorial(n):
    # base case: n is zero or one
    if n == 0 or n == 1:
        return 1
    # recursive case: return n times the factorial of n-1
    else:
        return n * rec_factorial(n-1)


if __name__ == "__main":
    number = int(input("Enter a number: "))
    print(factorial(number))
    print(rec_factorial(number))