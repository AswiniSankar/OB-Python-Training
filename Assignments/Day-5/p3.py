# printing list using For and while loop

numbers = [1, 2, 3, 4, 5]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
Num = ['222', '100', '85', '500', '300']

for i in numbers:
    print(i)
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
for i in range(len(weekdays)):
    print(weekdays[i])
i = 0
while i < len(weekdays):
    print(weekdays[i])
    i = i + 1
sum = 0
for i in Num:
    sum = sum + int(i)
print("The sum from for loop :", sum)
i = 0
sum = 0
while i < len(Num):
    sum = sum + int(Num[i])
    i = i + 1
print("The sum from while loop :", sum)
