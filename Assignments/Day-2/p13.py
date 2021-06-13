# print all unique vowels in the word
distinctvowel = []
word = input("enter the word")
for x in word:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        if word.count(x) == 1:
            distinctvowel.append(x)
print(distinctvowel)
