# program to remove duplicates in list with and without using set function
list = [12, 4, 90, 3, 12, 5, 6, 17, 3, 5, 9, 10, 6, 5, 90, 100]
s = set()
for i in list:  # with using set
    s.add(i)
print(s)
withoutduplicate = []
for i in list:  # without using set
    if i not in withoutduplicate:
        withoutduplicate.append(i)
print(withoutduplicate)
withoutduplicate.sort(reverse=True)
print(withoutduplicate)  # sorting in descending order
