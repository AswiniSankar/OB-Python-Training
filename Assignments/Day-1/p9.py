# program to find the given  two string is equal or else which is smaller and bigger
string1 = input("enter the string1")
string2 = input("enter the string2")
if string1 == string2:
    print("both strings are equal")
elif string1 > string2:
    print(string1 + " is greater " + string2 + " is smaller")
else:
    print(string1 + " is smaller " + string2 + " is greater")
