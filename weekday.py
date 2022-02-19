# This program asks the user to input a day in the week
# and then informs is it a weekend or not.
# Author: Eret Haava

days =  'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'

day = input('Please enter a weekday: ')

while day != days:
    if (day == 'Monday') or (day == 'Tuesday') or (day == 'Wednesday') or (day == 'Thursday') or (day == 'Friday'):
        print('Yes, unfortunately today is a weekday.')
        break
    elif (day == 'Saturday') or (day == 'Sunday'):
        print('It is the weekend, yay!')
        break
    else:
        print('Weekdays are Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday and not {}.\nTry again!' .format(day))
        day = input('Please enter a weekday: ')