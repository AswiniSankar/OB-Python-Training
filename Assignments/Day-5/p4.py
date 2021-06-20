# get the input from CLA to calculate BMI

from sys import argv


def toFindBMI(weight, height):
    return round(weight / (height * height), 1)


def BMIstatus(BMIvalue):
    if BMIvalue < 18.5:
        print("your BMI is " + str(BMIvalue) + " which means you are underweight")
    elif 18.5 <= BMIvalue and BMIvalue <= 24.9:
        print("your BMI is " + str(BMIvalue) + " which means you are healthy")
    elif 25.0 <= BMIvalue and BMIvalue <= 29.9:
        print("your BMI is " + str(BMIvalue) + " which means you are overweight")
    else:
        print("your BMI is " + str(BMIvalue) + " which means you are obese")


name = argv[1]
height = float(argv[2])
weight = float(argv[3])
print("Name : " + name + "\n" + "Height : " + str(height) + "\n" + "Weight : " + str(weight))
result = toFindBMI(weight, height)
BMIstatus(result)
