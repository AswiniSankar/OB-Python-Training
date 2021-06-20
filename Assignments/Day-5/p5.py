# program to standardizes the mobile number

def standardizes(func):
    def tocheck(phonenumbers):

        if len(str(phonenumbers)) == 10:

            print("+91 " + str(phonenumbers))
        else:

            func(phonenumbers)

    return tocheck


@standardizes
def check(phonenumber):
    print("+91 " + str(phonenumber)[2:])


n = int(input("enter the number of phone numbers"))
print("enter the list of phone numbers")
phonenumbers = []
for i in range(n):
    phonenumbers.append(int(input()))
print(phonenumbers)
phonenumbers.sort()
print(phonenumbers)
for i in range(n):
    check(phonenumbers[i])
