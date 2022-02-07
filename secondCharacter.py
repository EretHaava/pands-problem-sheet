# My solution to weekly task 03

# This program reads in a string and outputs 
# every n character of that string.
# You need to use Python's built-in function
# slice[start:stop:step] = slice[::n] to do that.
# n represent the character in the string.
# Because it's -2 (negative 2), the program starts
# counting from the end of the string.
# Author: Eret Haava

string = input("Enter a string: " )
n = -2
slice = string[::n]
print(slice)

# Or you can even make it shorter and use following program:
# string = input("Enter a string: " )
# n = -2
# print(string[::n])

# Example string:
# The quick brown fox jumps over the lazy dog.
    # Enter a string: The quick brown fox jumps over the lazy dog.
    # .o zletrv pu o wr cu h




