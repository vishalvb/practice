#decorators

def outer():
	messge = 'Hi'
	def inner():
		print(messge)
	return inner()

outer()