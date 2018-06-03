#Sorting List, Tuples, Objects

list = [5,3,6,7,8,1,2,0]

sorted_list = sorted(list, reverse = True)

print('original',list)
print('sorted', sorted_list)

list.sort(reverse = True)
print('orignial list.sort()', list) 

print('tuple sorting')
tup = (5,6,3,2,1)
print('orignial tuple',tup)
print('sorted', sorted(tup))


li = [-5,-4,1,5,0]
print('sorting using absolute value, key parameter',sorted(li, key = abs))

class Employee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary
	
	def __repr__(self):
		return '({},{},{})'.format(self.name, self.age, self.salary)
		
e1 = Employee('d',13, 35)
e2 = Employee('b',7, 74)
e3 = Employee('c',10, 65)

employees = [e1,e2,e3]

print('employees',employees)
print('sort according to name', sorted(employees, key = lambda e:e.name))
print('sort according to age', sorted(employees, key = lambda e:e.age))
print('sort according to salary', sorted(employees, key = lambda e:e.salary))


from operator import attrgetter
print('sort using attrgetter', sorted(employees, key = attrgetter('salary')))



