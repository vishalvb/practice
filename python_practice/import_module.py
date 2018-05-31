#import module

print('import my own module')
test = 'test string'

def find_index(to_search, target):
	'''find the index in a sequence'''
	for i, value in enumerate(to_search):
		if value == target:
			return i
		
	return -1