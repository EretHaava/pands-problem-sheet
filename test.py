days =  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']

day = input('Please enter a weekday: ')

while day != days:
    if day == [weekdays]:
        print('Yes, unfortunately today is a weekday.')
        break
    elif day == [weekend]:
        print('It is the weekend, yay!')
        break
    else:
        print('Weekdays are Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday and not {}.\nTry again!' .format(day))
        day = input('Please enter a weekday: ')
        