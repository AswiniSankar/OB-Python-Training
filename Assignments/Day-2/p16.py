# program to print sum of values in dictionary
temp = 1
dict = {}
while temp == 1:
    numbers = eval(input("enter the number"))
    value = eval(input("enter the value"))
    dict[numbers] = value
    temp = eval(input("press 1 to continue "))
print(dict)
sum = 0
for v in dict.values():
    sum = sum + v
print("the sum of values in dictionary is " + sum)
