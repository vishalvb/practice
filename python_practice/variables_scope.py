#Variables scoping
'''
LEGB
Local, Enclosing, Global, Built-in
'''
import builtins


x = 'global x'

def test():
	x = 'local x'
	print (x)

test()

'''overrite global value'''
def change():
	global x
	x = 'local'
	
change()
print(x)

#print(dir(builtins))

def outer():
	y = 'outer y'
	
	def inner():
		'''enclosing scope'''
		nonlocal y
		print(y)
		y = 'edited'
	inner()
	print(y)
outer()














