# get the input from user for tuple and print the sum and average

n = eval(input("enter the value"))
sum = 0
val = tuple(x for x in n)
print(val)
for i in val:
    sum = sum + i
print(sum)
