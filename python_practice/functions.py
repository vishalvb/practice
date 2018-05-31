#functions

def hello():
	return 'World'

print(hello().upper())

def greet(greet, name = 'blank'):
	return '{},{} hello'.format(greet, name)

print(greet('vishal', 'noname'))

def info(*arg, **args):
	print(arg)
	print(args)
	
courses = [1,2,3]
info1 = {'name':'abc','age':5}
	
info(1,2,3, name = 'vishal')
info(courses,info1)
info(*courses,**info1)
