# Ryan Lugo: RJL 12/9/21

height_feet = int(input("What's is your current height in feet?: "))
height_inches = int(input("What's your current height with inches?: "))
weight = int(input("What's your current weight in lbs?: "))


def bmi_calculate(feet,inches,weight):
    weight_convert = weight / 2.205

    height_feet_to_inches = (feet * 12) + inches
    height_convert = height_feet_to_inches / 39.37

    bmi = weight_convert / (height_convert ** 2)
    bmi_info = "nil"

    if bmi < 19:
        bmi_info = "Underweight"
    elif bmi < 25:
        bmi_info = "Healthy"
    elif bmi < 30:
        bmi_info = "OverWeight"
    elif bmi < 40:
        bmi_info = "Obese"
    elif bmi > 40:
        bmi_info = "Extremely Obese"
    return bmi_info

print(bmi_calculate(height_feet,height_inches,weight))
