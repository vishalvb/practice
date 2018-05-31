import import_module
import sys
import random
import datetime
import calendar
import os

print(os.getcwd())

'''print sys path'''
#print(sys.path)

print('today is', datetime.date.today())
courses = ['ML','AI','NLP']

index = import_module.find_index(courses,'ML')
print(index)
print(import_module.test)

print(random.choice(courses))
