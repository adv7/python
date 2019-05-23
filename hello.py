
from my_module import find_index
import random
import math
import datetime
import calendar
import os


courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)

#print(sys.path)

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

print(os.getcwd())
