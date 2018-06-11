#erros and exceptions

try:
	a  =10
	f = open('file.txt')
except Exception as e:
	print('in exception block, sorry this file does not exist', e)
else:
	print(' in else block, no exception occured')
finally:
	print('in finally block which would definietly run')
	