# program to find BMI status

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


name = input("what is your name? ")
height = float(input("Hai " + name + ", What is your Height in meters? "))
weight = float(input("What is your weight in kg? "))
result = toFindBMI(weight, height)
BMIstatus(result)
