# pands-problem-sheet

Solution to week 02

To find materials, on how to calculate your BMI in Python, wasn't a problem at all.
I used following sources:
1) Youtube
2) Google    
There were loads of different videos in Youtube and materials in Google.

However, the formula to calculate your BMI was always same:
bmi = weight / height**2
Pay attention that in the weekly task, we were asked to enter the weight in kg and the height in cm!!! Therefore, you have to options:
1) convert cm into meters and then continue, or
2) change the formula a bit: bmi = weight/(height/100)**2
Both do exactly the same job.

I also used Pythons built-in function round() here, because BMI like 21,753135271392187
didn't look very neat. Full number looked much better.

I added in an extra bit to inform the user if he/she is underweight, normal weight,
overweight or obese. Good to know... Should you worry and start moving now 
or you can be lazy on a couch another while.



Solution to week 03

To be honest, it took a while to figure that out...
I had to reverse the string and then slice it. 

I used following sources: 
1) Google
2) Youtube - wasn't really much help this time
3) https://realpython.com/reverse-string-python/
4) https://docs.python.org/3/library/functions.html
5) https://www.w3schools.com/python/python_howto_reverse_string.asp

Unfortunately I started first with slicing.
Python has a built-in function called slice[start:stop:step] = slice[::n].
n represent in every which character you need to get from that string.
Keep in mind that one empty space between the caracters in that strings counts as one character.

string = input('Enter a string: ')
n = 2
slice = string[::n]
print(slice)

I should have tried to make n negative and my search for solution would have finished there and then. Unfortunately I didn't do that and...

...next I was looking for a program how to reverse a string.
Python has a built-in function called reversed (reversed[::-1]).
I used following program to do that.

string = input('Enter a string: ')
reversed = string
n = -1 
print(reversed[::n])

So... I had two programs that looked quite alike. How to merge them? 
Or is there any need to merge them? And then it hit me!
One small change (make n negative) in first program (slicing)
gave me an answer I was looking for...

So, here's the program I used to complete weekly task.
It reads in a string and outputs every second character of that string in reversed order.

string = input("Enter a string: " )
n = -2
slice = string[::n]
print(slice)

Or you can even make it shorter and use following program:

string = input("Enter a string: " )
n = -2
print(string[::n])

Example string: The quick brown fox jumps over the lazy dog.
    Enter a string: The quick brown fox jumps over the lazy dog.
    .o zletrv pu o wr cu h


Solution to week 04