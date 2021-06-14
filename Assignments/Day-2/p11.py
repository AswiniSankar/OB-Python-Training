# to print the nested list matrix from
n, m = eval(input())
list1 = []
for i in range(n):
    list2 = []
    for j in range(m):
        list2.append(eval(input()))
    list1.append(list2)
for i in range(n):
    for j in range(m):
        print(list1[i][j], end=" ")
    print()
print("------------*********---------")
list3 = [[1, 2, 3], [4, 5, 6, ], [7, 8, 9]]
for x in list3:
    print(*x)
