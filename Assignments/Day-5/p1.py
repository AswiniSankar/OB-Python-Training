# python program to calculate BMI of Argo


def BMIOfArgo(weight, height):
    return (weight / (height * height))


age = int(input("Hai Arge, what is your Age?"))
weight = float(input("What is your weight in kg ?"))
height = float(input("What is your Height in meters"))
print("The MBI is {:.1f}".format(BMIOfArgo(weight, height)))
