#Generators

def square(nums):
	for i in nums:
		yield (i*i)

my_list = square([1,2,3,4])
print(my_list)
for i in my_list:
	print(i)
	
my_list = (x * x for x in [1,3,5])
print(type(my_list))
print('generator',my_list)
for i in my_list:
	print(i)
	