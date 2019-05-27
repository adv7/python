
from my_module import find_index
import random
import math
from datetime import datetime
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

# today = datetime.date.today()
# print(today)

print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)
print(os.listdir())

# os.chdir('C:/Users/cud4x/PycharmProjects/my_module_to_import')
# os.mkdir('newDir')
# os.makedirs('outsideDir/insideDir')
# os.rmdir('newDir')
# os.removedirs('outsideDir/insideDir')
# os.rename('hello.py', 'asd.py')


# print(os.stat('my_module.py').st_size)
# mod_time = os.stat('my_module.py').st_mtime
# print(datetime.fromtimestamp(mod_time))

# for dirpath, dirnames, filenames in os.walk('C:/Users/cud4x/PycharmProjects/my_module_to_import'):
#     print('Current Path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files:', filenames)
#     print()

# os.chdir('/Users/cud4x/Desktop')
# print(os.environ.get('hello.py'))
# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

# print(file_path)

# os.path.basename('/path/file.txt')
# os.path.split('/path/file.txt')
# os.path.exists('/path/file.txt')
# os.path.isfile('/path/file')
# os.path.splitext('/path/file.txt')
# print(dir(os.path))

