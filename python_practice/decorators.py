#decorators

def decorator(myfunc):
	def wrapper(*args):
		return myfunc(*args)
	return wrapper


@decorator
def display():
	print('display function')

	
@decorator
def info(name, age):
	print('name is {} and age is {}'.format(name,age))

info('john', 23)
#hi = decorator(display)
#hi()
display()