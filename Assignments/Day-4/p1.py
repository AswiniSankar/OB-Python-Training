# program to print the given string for n number of times

def checkfornegative(func):
    def tocheck(statement, number):
        if number < 0:
            print("please provide a positive number")
        else:
            func(statement, number)

    return tocheck


@checkfornegative
def toprint(statement, number):
    print("OUTPUT:")
    for i in range(number):
        print(statement)


statement = input("enter the string that you want to print")
number = int(input("how many times you want to print the statement"))
toprint(statement, number)
