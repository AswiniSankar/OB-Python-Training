# program to find the given year is leap year or not

year = int(input("enter the year"))
if 1900 <= year and year <= 100000:
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                # print("{0} is a leap year".format(year))
                print("True")
            else:
                # print("{0} is not a leap year".format(year))
                print("Flase")
        else:
            # print("{0} is a leap year".format(year))
            print("True")
    else:
        # print("{0} is not a leap year".format(year))
        print("Flase")
