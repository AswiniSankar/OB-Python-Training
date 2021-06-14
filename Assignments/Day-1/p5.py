# program to remove duplicates in the given string

from collections import Counter


def removeduplicate1(string):  # using counter
    wordcount = Counter(string)
    for k, v in wordcount.items():
        if v >= 1:
            print(k, end="")


def removeduplicate2(string):
    x = set()
    for i in string:
        x.add(i)
    print(*x)


def removeduplicate3(string):
    duplicate = []
    for i in string:
        if string.count(i) >= 1:
            if i not in duplicate:
                duplicate.append(i)
    print(*duplicate)


string = input("enter the string")
removeduplicate1(string)  # using counter
print()
removeduplicate2(string)  # using set
removeduplicate3(string)  # using count and list
