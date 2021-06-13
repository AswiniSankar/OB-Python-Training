# program to find maximum of three numbers
a, b, c = eval(input("enter three values"))
max = a if a > b and a > c else b if b > c else c
print("the maximum value is " + str(max))
