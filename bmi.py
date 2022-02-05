# My solution to weekly task 02

# This program takes in your height in cm,
# your weight in kg and outputs your BMI.
# It also tells you are you underweight,
# normal weight, overweight or obese.
# Author: Eret Haava

print ('Hello!\nThis is BMI calculator.')
name = input('Enter your name? ')
print ('Hello ' + name + '!')
weight = float(input('Enter your weight (kg): '))
height = float(input('Enter your height (cm): ')) 
bmi = weight / (height/100)**2

# If you want your BMI to be full number, use 
# Python's built-in function round(), and replace
#   bmi = weight / (height/100)**2
#   with
#   bmi = round(weight / (height/100)**2)

# If you want the output to be only BMI, use this code
print('Your BMI is {}.' .format(bmi))

# If you want to know are you underweight, normal weight,
# overweight or obese, add following onto your code.
#if bmi <= 18.5:
#    print('Your BMI is {}, which means you are underweight.' .format(bmi))
#if bmi > 18.5 and bmi < 24.9:
#    print('Your BMI is {}, which means you are normal weight.' .format(bmi))
#if bmi > 25 and bmi < 29.9:
#    print('Your BMI is {}, which means you are overweight.' .format(bmi))
#if bmi > 30:
#    print('Your BMI is {}, which means you are obese.' .format(bmi))