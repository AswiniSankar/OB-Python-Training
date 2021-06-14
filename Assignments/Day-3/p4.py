# program to generate a fibonacci series
def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        a, b = 0, 1
        print(a, b, end=" ")
        for x in range(2, n):
            c = a + b
            print(c, end=" ")
            a = b
            b = c


n = int(input("enter the number"))
fibo(n)
