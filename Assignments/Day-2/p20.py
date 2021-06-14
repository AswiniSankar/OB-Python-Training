# to find distinct average weight
n = eval(input("enter the value for n"))
list = []
s = set()
print("enter the weight of " + str(n) + " person")
for i in range(n):
    weight = eval(input())
    list.append(weight)
    s.add(weight)
sum = 0
count = 0
for i in s:
    sum = sum + i
    count = count + 1
print(sum)
print("average is " + str(sum / count))
