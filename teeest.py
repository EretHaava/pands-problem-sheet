days = ('Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
)

from datetime import date
import calendar
curr_date = date.today()
#print(calendar.day_name[curr_date.weekday()])

if days == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday':
    print('It is the weekend, yay!')
else:
    print('Yes, unfortunately today is a weekday.')