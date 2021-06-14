# read list from user and sort it in descending order
n = int(input())
list1 = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
print(list1)
list1.sort(reverse=True)
print(list1)
