# program to generate otp of 6 digit combination of alpha numeric alternatively
import random

alpha = []
for i in range(26):
    alpha.append(chr(i + ord('a')))
digit = list(range(0, 10))
print(alpha[random.randint(0, 25)] + str(digit[random.randint(0, 9)]) +
      alpha[random.randint(0, 25)] + str(digit[random.randint(0, 9)]) + alpha[random.randint(0, 25)] +
      str(digit[random.randint(0, 9)]))
