# program to find relation between two numbers using ternary operator
a, b = eval(input("enter two number"))
result = "equal" if a == b else "greater than " if a > b else "lesser than"
print(str(a) + " is " + result + " " + str(b))
