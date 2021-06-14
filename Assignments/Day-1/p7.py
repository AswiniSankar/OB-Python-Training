# reverse word by word
def reveserbyword(string):
    splitlist = []
    splitlist = string.split(" ", len(string))
    # print(*splitlist)

    str = " "
    for x in splitlist:
        str = str + x[::-1] + " "
    return str


string = input("enter the string")
print(reveserbyword(string))  # using split function
