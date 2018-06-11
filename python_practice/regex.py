#Regular Expression
import re

text = '''
abcdefhijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha Hahahaha

mywebsite.com

Meta characters needs to be escaped 
301-549-9718
123-456-1231

Mr. Vishal Bahedia
'''


sentence = 'start a sentence and bring it to front of the end'
pattern = re.compile(r'abc')
matches = pattern.finditer(text)
print('\nfinding abc')
for match in matches:
	print(match)
print('\nfinding Ha with word boundary before it')
pattern = re.compile(r'\bHa')
matches = pattern.finditer(text)

for match in matches:
	print(match)

	
print('\nusing ^ means it should be at start of the string')
print(sentence)
pattern = re.compile(r'^start')
matches = pattern.finditer(sentence)
for match in matches:
	print(match)

	
	
print('\nusing $ means it should be at the end of the string')
print(sentence)
pattern = re.compile(r'end$')
matches = pattern.finditer(sentence)
for match in matches:
	print(match)

	
print('\n matching the phone number')
pattern = re.compile(r'\d+.\d+.\d+')
matches = pattern.finditer(text)
for match in matches:
	print(match)