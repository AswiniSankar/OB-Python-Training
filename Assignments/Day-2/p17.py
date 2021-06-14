# read input from user and form a dictionary
import sys

dict = {}
while True:
    print("1.add elements 2. display elements 3.to know mark 4.exit")
    print("enter your choice")
    choice = eval(input())
    if choice == 1:
        sname = input("enter student name")
        smark = input("enter the student mark")
        dict[sname] = smark
    elif choice == 2:
        flag = 0
        for k, v in dict.items():
            flag = 1
            print(k, v)
        if flag == 0:
            print("dictonary is empty")
    elif choice == 3:
        flag = 0
        name = input("enter the student name to whom you want to know mark")
        for k, v in dict.items():
            if k == name:
                print(k + " secured " + v + " mark")
                flag = 1
        if flag == 0:
            print("student not found ")
    elif choice == 4:
        sys.exit()
    else:
        print("invalid option")
