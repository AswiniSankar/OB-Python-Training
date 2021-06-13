# program to reverse a given string
string = input("enter the string that you want to reverse")
print(string[:: -1])  # using slice
str = ""


def reverse(string):  # using recursion
    string = "".join(reversed(string))
    return string


for x in string:  # using loop
    str = x + str
print(str)
print(reverse(string))
