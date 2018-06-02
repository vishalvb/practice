#First Class Functions

def square(x):
	return x*x

def my_map(func, list):
	result = []
	for n in list:
		result.append(func(n))
	return result

squares = my_map(square, [1,2,3])
print(squares)


def html_tag(tag):
	def wrap_t(msg):
		print('<{0}>{1}</{0}>'.format(tag, msg))
	return wrap_t

h1 = html_tag('h1')
print(h1('text'))