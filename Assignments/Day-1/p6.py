# print count of each character in the string
from collections import Counter


def countchar1(string):
    lettercount = Counter(string)
    for k, v in lettercount.items():
        print(str(k) + " ------> " + str(v))


def countchar2(string):
    charpresent = []
    for char in string:
        if string.count(char):
            if char not in charpresent:
                charpresent.append(char)
                charpresent.append(string.count(char))
    print(charpresent)


string = input("enter the string")
countchar1(string)  # using counter
countchar2(string)  # using count
