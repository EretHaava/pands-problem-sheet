# My solution to weekly task 02

# This program greets you and calculates your BMI.
# It tells you what weight you are.
# Author: Eret Haava

print ('Hello!\nThis is BMI calculator.')
name = input('What is your name? ')
print ('Hello ' + name + '!')
height = float(input('Enter your height in cm: ')) 
weight = float(input('Enter your weight in kg: '))
bmi = weight / (height/100)**2

# If you want your BMI to be full number, use round
# bmi = round(weight / (height/100)**2)

# If you want only BMI, use this code
# print('Your BMI is + {}' .format(bmi))
# If you want to know are you normal weight or not,
# use the following code.

if bmi <= 18.5:
    print('Your BMI is {}, which means you are underweight.' .format(bmi))
if bmi > 18.5 and bmi < 24.9:
    print('Your BMI is {}, which means you are normal weight.' .format(bmi))
if bmi > 25 and bmi < 29.9:
    print('Your BMI is {}, which means you are overweight.' .format(bmi))
if bmi > 30:
    print('Your BMI is {}, which means you are obese.' .format(bmi))