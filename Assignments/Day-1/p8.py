# program to check wherether the sub-string is present the main string
string = input("enter the string")
substring = input("enter the sub string")
'''print(string.find(substring))
print(string.index(substring))
print(string.rfind(substring))'''
if (string.find(substring) == -1):
    print("sub string not present in  main string")
else:
    print("sub string present in main string")
