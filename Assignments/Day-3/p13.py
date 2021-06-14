# program to print the values based upon values in the charcter array with dictionary
dic = {'a': "Apple", 'd': "Digit", 'u': "Union", 'T': "Temple", 'Q': "Quuen", 'R': "rabbit", 's': "snake"}
char_array = ['a', 'r', 'T', 's']
for k, v in dic.items():
    if k in char_array:
        print(v)
