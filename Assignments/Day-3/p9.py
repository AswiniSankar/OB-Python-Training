# program to find list of rational number multiplication
from functools import reduce


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def multiplication(n, list1, list2):
    new_num = 1
    new_dem = 1
    for i in range(0, n):
        new_num = new_num * list1[i]
        new_dem = new_dem * list2[i]
    GCD = gcd(new_num, new_dem)
    new_num = new_num / GCD
    new_dem = new_dem / GCD
    print(int(new_num), "/", int(new_dem))


list1 = list(int(x) for x in input("enter the numerator list  values").split(','))
print(list1)
list2 = list(int(x) for x in input("enter the denominator  list values").split(','))
print(list2)
n = len(list1)
multiplication(n, list1, list2)

