checksum = input("Enter a checksum: ")
checkDigit = int(checksum[len(checksum)-1])
cntDigit = len(checksum)-1
control = 0
n = 0
for i in range(cntDigit):
    control += int(checksum[n])
    n += 1
if (control % 10) == checkDigit:
    print("VALID")
else:
    print("INVALID")