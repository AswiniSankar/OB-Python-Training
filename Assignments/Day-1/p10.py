# program to reverse the word not character
def reversestring(string):
    string = string.split(" ")[:: -1]
    print(*string)


string = input("enter the string")
reversestring(string)
