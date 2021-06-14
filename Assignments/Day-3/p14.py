# Python program to convert time  from 12 hour to 24 hour format

def convert24(s):
    # Get hours
    h1 = ord(s[1]) - ord('0')
    h2 = ord(s[0]) - ord('0')
    hh = (h2 * 10 + h1 % 10)

    # If time is in "AM"
    if (s[8] == 'A'):
        if (hh == 12):
            print('00', end='')

            for i in range(2, 8):
                print(s[i], end='')

        else:
            for i in range(0, 8):
                print(s[i], end='')

    # If time is in "PM"
    else:
        if (hh == 12):
            print("12", end='')

            for i in range(2, 8):
                print(s[i], end='')

        else:
            hh = hh + 12;
            print(hh, end='')

            for i in range(2, 8):
                print(s[i], end='')


time = input("enter the time in the format of hh:mm:ss AM/PM")
convert24(time)
