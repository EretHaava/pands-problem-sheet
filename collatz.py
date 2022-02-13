# This program uses Collatz conjecture.
# It asks the user to input positive integer.
# If the number is even, it divides it by two.
# If the number is odd, it multiplies it by three and adds one.
# The program keeps running until the current value is one.
# Author: Eret Haava

def collatz(number):
    if (number % 2 == 0):       # checks for even number
        return number // 2      # performs mathematical operation
    elif (number % 2 == 1):     # checks for odd number
        return number * 3 + 1   # performs mathematical operation

number = int(input('Please enter a positive integer: '))
print(number)       # prints out input number
while(number != 1):     # goes through this loop until condition is True
    number = collatz(number)    # performs Collatz conjecture
    print(number)   # prints out the list


    