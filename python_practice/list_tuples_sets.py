#List, Tuples, and Sets

courses = ['ML', 'AI', 'NLP', 'Algorithms']
print(courses)
print(courses[0])
print(courses[-1])
courses.append('Data Mining')
print('After appending', courses)

courses.insert(0,'Data Structures')

print('After Inserting',courses)

more = ['Data','DBMS']
courses.extend(more)
print('AFter Extending', courses)

popped = courses.pop()

print('popped',popped)
print('after popping',courses)

courses.reverse()

print('after reverse', courses)

courses.sort()

print('after sort', courses)

print('find', courses.index('ML'))

print('each item in list using for loop')
for items in courses:
	print(items)

print('each item in list using for loop and enumerate')
for index, course in enumerate(courses):
	print(index, course)
	

course_str = ','.join(courses)
print('joined string', course_str)
	

num = [1,2,3,4,5]
print('num list', num)
print('minimum from list',min(num))
print('max fro list', max(num))
print('sum of list', sum(num))
print()
print('TUPLES -- Immutable')
tuple_1 = (1,2,3)
tuple_2 = tuple_1

print(tuple_2)

print('SETS -- Unordered and No Duplicates')

set_1 = {'ML','AI','NLP','Algo','ML'}
set_2 = {'ML','Data'}
print('set_1',set_1)
print('set_2',set_2)
print('intersection',set_1.intersection(set_2))
print('union',set_1.union(set_2))
print('difference',set_1.difference(set_2))
