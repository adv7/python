import datetime
import pytz

# tday = datetime.date.today()
# print(tday.weekday())
# print(tday.isoweekday())
#
# tdelta = datetime.timedelta(days=7)
# tdelta_2 = datetime.timedelta(hours=12)
#
# print(tday + tdelta)
# print(tday - tdelta)
#
# # date2 = date1 + timedelta
# # timedelta = date1 + date2
#
# bday = datetime.date(2019, 7, 27)
# till_bday = bday - tday
#
# print(till_bday.days)
# print(till_bday.total_seconds())
#
# t = datetime.time(10, 42, 12, 100000)
# print(t)
#
# dt = datetime.datetime(2019, 10, 12, 12, 35, 12, 0)
# print(dt)
# print(dt.year)
#
# print(dt + tdelta)
# print(dt + tdelta_2)

dt = datetime.datetime(2019, 10, 12, 12, 35, 12, tzinfo=pytz.UTC)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now(tz=pytz.UTC)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

print('dt_today: \t', dt_today)
print('dt_now: \t', dt_now)
print('dt_utcnow: \t', dt_utcnow)
print()

# dt_pol_2 = datetime.datetime.now()
# pol_tz = pytz.timezone('Poland')
#
# dt_pol_2 = pol_tz.localize(dt_pol_2)
# print('Time in poland: \t', dt_pol_2)

# dt_pol = dt_utcnow.astimezone(pytz.timezone('Poland'))
# print('Time in poland: \t', dt_pol)

# for tz in pytz.all_timezones:
#     print(tz)

dt_pol_3 = datetime.datetime.now(tz=pytz.timezone('Poland'))
print('Time in poland: \t', dt_pol_3.strftime('%B %d, %Y'))

dt_str = 'May 28, 2019'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print('Convert back: \t', dt)

# strftime - datetime to string
# strptime - string to datetime
