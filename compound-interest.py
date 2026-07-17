principle=float(input("Enter principle amount: "))
rate=float(input("Enter rate (%): "))
time=float(input("Enter the time (years): "))
A=principle *(1 + rate/100)**time
CI=A-principle
print("The CI is: ",CI)