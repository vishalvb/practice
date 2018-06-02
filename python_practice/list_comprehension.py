#List comprehensions

print('list comprehensions')
nums = [1,2,3,4,5,6,7,8,9]
'''
my_list = []
for n in nums:
	my_list.append(n)
print(my_list)
'''
my_list = [n for n in nums]
print(my_list)

my_list = [n * n for n in nums]
print(my_list)

my_list = [n * n for n in nums if n%2 ==0]
print(my_list)

my_list = []
for i in range(4):
	for letter in 'abc':
		my_list.append((i, letter))
print(my_list)

my_list = [(letter, num) for num in range(4) for letter in 'abc']
print(my_list)


names = ['bat', 'super','iron']
hero = ['man','woman','ore']
'''
my_dict = {}
for names, hero in zip(names, hero):
	my_dict[names] = hero

print(my_dict)

my_dict = {}'''
my_dict = {name:heros for name, heros in zip(names, hero)}
print(my_dict)


nums = [1,1,2,2,3,3,4,4,5]
my_set = set()

my_set = {n for n in nums}
print('set', my_set)




