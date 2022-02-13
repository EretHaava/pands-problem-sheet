# This program uses Collatz conjecture.
# It asks the user to input positive integer.
# If the number is even, it divides it by two.
# If the number is odd, it multiplies it by three and adds one.
# The program keeps running until the current value is one.
# Author: Eret Haava



number = int(input('Please enter a positive integer: '))

def collatz(number):
    if (number % 2 == 0):
        return number // 2
    elif (number % 2 == 1):
        return number * 3 + 1

print(number)       # prints out input number

while(number != 1):
    number = collatz(number)
    print(number)   # prints out the list

