# program for string validation

str = input("enter the string")

if str.isalnum():
    print("True")
else:
    print("false")

result1 = any(x.isalpha for x in str)

result2 = any(x.isdigit() for x in str)

result3 = any(x.islower() for x in str)

result4 = any(x.isupper() for x in str)

if result1:
    print("True")
else:
    print("false")
if result2:
    print("True")
else:
    print("false")
if result3:
    print("True")
else:
    print("false")
if result4:
    print("True")
else:
    print("false")
