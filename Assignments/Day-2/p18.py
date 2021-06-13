# program to find number of occurence of each character  in tha string
from collections import Counter

string = input("enter the string")
occurence = Counter(string)
for k, v in occurence.items():
    print(k + " --> ", v)
