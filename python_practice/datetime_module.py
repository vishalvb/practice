#datetime module

import datetime

d = datetime.date(2018,6,4)
print('date is', d)

tod  = datetime.date.today()
print('today year is {}, day is {}, weekday is{}'.format( tod.year, tod.day, tod.weekday()))

tdelta = datetime.timedelta(days = 7)

print('time delta 7 days', tod + tdelta)

#date2 = date + timedelta
#timedelta = date2 - date2

d1 = datetime.date(2018, 5, 4)

print('difference of two dates',d1 - d)

print('working with time')

t = datetime.time(9,55,23)
print('time is', t)
aware = datetime.datetime(2016,6,4, 9, 57, 25)
print('working with aware time', aware)
print('only date from aware date time', aware.date())
print('only time from aware date time', aware.time())

print('working with time zone')
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print('today', dt_today)
print('now',dt_now)
print('utcnow', dt_utcnow)


import pytz
dt  = datetime.datetime(2016,6,4,10,6,23,tzinfo = pytz.UTC)
print('time is ', dt)




















