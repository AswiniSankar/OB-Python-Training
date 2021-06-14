# filter the even numbers from list with and without using lambda functions
def iseven(num):
    return num % 2 == 0


list1 = [3, 2, 1, 8, 10, 2, 5, 190, 26, 134]
lis2 = list(filter(lambda x: (x % 2) == 0, list1))
print(lis2)
lis2 = list(filter(iseven, list1))
print(lis2)
