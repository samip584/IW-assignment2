# Write an if statement to determine whether a variable holding a year
# is a leap year.

year = 2019

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
