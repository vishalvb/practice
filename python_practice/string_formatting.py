#string formatting

person = {'name':'john','age':25}
sentence = 'my name is {} and age is {}'.format(person['name'],person['age'])
print(sentence)

tag = 'h1'
text = 'this is the text'

sentence = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence)

sentence = 'my name is {0[name]} and age is {0[age]}'.format(person)
print('sentence',sentence)

class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age
p1 = Person('jony',25)
sentence = 'ny name is {0.name}, and age is {0.age}'.format(p1)
print('sentence using class',sentence)

sentence = 'ny name is {name}, and age is {age}'.format(name = 'jon', age = 25)
print('sentence using dictionary',sentence)

sentence = 'ny name is {name}, and age is {age}'.format(**person)
print('sentence using ',sentence)


for i in range(5):
	p = 'the value is {:02}'.format(i)
	print(p)

import datetime

my_date = datetime.datetime(2018,6,3,12,12,12)
print('date is', my_date)

print('formatting date {:%B, %d, %Y, %A, %j}'.format(my_date)) 