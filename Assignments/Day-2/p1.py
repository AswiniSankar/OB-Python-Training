# conditional action in the given integer

n = int(input("enter the number"))
if 1 <= n and n <= 100:
    if n % 2 == 1:
        print("Weird")
    elif (n % 2 == 0) and (2 <= n and n <= 5):
        print("Not Weird")
    elif (n % 2 == 0) and (6 <= n and n <= 10):
        print("Weird")
    elif (n % 2 == 0) and (n > 20):
        print("Not Weird")
