'''using list comprehension
  1. print power of 2 in range(1,10)
  2. print squares in range(1,15)
  3. print double of number range (1,40) and number should be even
'''
list1 = list(x ** 2 for x in range(1, 10))
print(list1)
list2 = list(x * x for x in range(1, 15))
print(list2)
list3 = list(x + x for x in range(1, 40) if (x + x) % 2 == 0)
print(list3)
