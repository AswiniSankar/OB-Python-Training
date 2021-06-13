# program to find number of occurence of vowels present in the string

string = input("enter the string")
vowelcount = []
for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        if i not in vowelcount:
            vowelcount.append(i)
            vowelcount.append(" --> ")
            vowelcount.append(string.count(i))
            vowelcount.append(", ")
print(*vowelcount)
