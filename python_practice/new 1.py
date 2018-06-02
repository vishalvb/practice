#closure

def outer():
	message = 'Hi'
	def inner():
		print(message)
	return inner

outer()
		