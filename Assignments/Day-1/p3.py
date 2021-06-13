# program to find sum of first n numbers
n = eval(input("enter the number"))
sum = 0
for x in range(1, n + 1):
    sum = sum + x
print("the sum of first 'n' number is " + str(sum))
