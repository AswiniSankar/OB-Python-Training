# program to print the upcoming character
# eg: input =b4n1 ; output = fo
string = input("enter the string")
for x in range(1, len(string), 2):
    print(chr(ord(string[x - 1]) + int(string[x])), end="")
