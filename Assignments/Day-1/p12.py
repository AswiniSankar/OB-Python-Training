# merge 2 strings into by merging character alternatively
string1 = input("enter the string1")
string2 = input("enter the string2")
min = len(string1) if len(string1) <= len(string2) else len(string2)
newstring = ""
for i in range(min):
    newstring = newstring + string1[i] + string2[i]
if len(string1) == len(string2):
    print(newstring)
elif len(string1) > len(string2):
    print(newstring + string1[min:])
else:
    print(newstring + string2[min:])
