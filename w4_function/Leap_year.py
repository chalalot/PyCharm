year = int(input("enter your year: "))
while year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
    break

if year % 4 != 0:
    print(year, "is not a leap year")
