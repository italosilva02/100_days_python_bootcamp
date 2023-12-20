'''
Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.
'''

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height**2)

def bmi_calculate(x):
    if x < 18.5:
        print(f'Your BMI is {x}, you are underweight.')
    elif x >= 18.5 and x < 25:
        print(f'Your BMI is {x}, you have a normal weight.')
    elif x >= 25 and x < 30:
        print(f'Your BMI is {x}, you are slightly overweight.')
    elif x >= 30 and x < 35:
        print(f'Your BMI is {x}, you are obese.')
    else:
        print(f'Your BMI is {x}, you are clinically obese.')

bmi_calculate(bmi)

'''
Resposta:

height = float(input())  # in meters e.g., 1.55
weight = int(input())  # in kilograms e.g., 72
# Your code below this line 👇
bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
'''