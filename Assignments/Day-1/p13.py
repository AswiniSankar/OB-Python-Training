# program to print the number of times the character in string
string = input("enter the value")
for x in range(1, len(string), 2):
    temp = int(string[x])
    temp1 = string[x - 1] * temp
    print(temp1, end="")
print()
for x in range(1, len(string), 2):
    print(string[x - 1:x] * int(string[x]), end="")
print()
