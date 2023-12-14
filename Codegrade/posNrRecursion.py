def rec_print(n):
    # base case: n is less than or equal to zero
    if n < 0:
        return
    # recursive case: print n and call rec_print with n-1
    else:
        rec_print(n-1)
        print(n)


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    rec_print(number)
