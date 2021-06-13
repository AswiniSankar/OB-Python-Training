# program to print character fristby possition then by odd possition
string = input("enter the string")
print(string[1::2] + string[::2])
for x in range(1, len(string), 2):
    print(string[x], end="")
for x in range(0, len(string), 2):
    print(string[x], end="")
