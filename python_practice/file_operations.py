#file operations

with open('test.txt', 'r') as f:
	#print('file contents using f.read()', f.read())
	#print('file contencts using f.readlines()', f.readlines())
	#print('file read 1 line using f.readline', f.readline())
	print('read line by line, so that there is no memeory issue')
	for line in f:
		print(line, end = '')

print()
with open('test.txt', 'r') as f:
	print('printing using specific size')
	size_to_read = 10
	
	f_contents = f.read(size_to_read)
	while len(f_contents) > 0:
		print(f_contents, end = '*')
		f_contents = f.read(size_to_read)
	
print('WRITING to a file')
with open('test1.txt', 'w') as f:
	f.write('test file')