#Dictionary -- (Key, Value) Pair
print('Dictionary tutorials')

student = {'name':'vishal','age':27,'courses':['ML','AI']}
print(student)
print(student['courses'])

student.update({'name':'Vishal'})
print(student)

for key,value in student.items():
	print(key,value)
