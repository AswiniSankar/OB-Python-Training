# program to find nth fibonacci number
def fibo(n):
    if n == 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


n = int(input("enter the number"))
print(fibo(n))
