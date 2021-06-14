# to find runner up in the annual sports day

n = int(input("enter the number of participant"))
scores = list(map(int, input("enter the score ").split(",")))[:n]
# print(scores)
withoutduplicates = []
for x in scores:
    if x not in withoutduplicates:
        withoutduplicates.append(x)
withoutduplicates.sort()
print(withoutduplicates[2])
