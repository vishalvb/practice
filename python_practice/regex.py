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
123.456.1231

cat
mat
bat



Mr. Vishal Bahedia
Mr First Last
Mrs Mfirst Mlast

Mrs. Anyfirst Anylast
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
pattern = re.compile(r'\d+[.]\d+[.]\d+')
matches = pattern.finditer(text)
for match in matches:
	print(match)

	
print('using ^ inside the [] will negate the operation')
print(sentence)
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text)
for match in matches:
	print(match)

	
	
print('\n matching the phone number')
pattern = re.compile(r'\d{3}[.]\d{3}[.]\d{4}')
matches = pattern.finditer(text)
for match in matches:
	print(match)

print('\n matching names')
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*\s\w*')
matches = pattern.finditer(text)
for match in matches:
	print(match)

	
	
emails = '''
vishalbahedia@gwmail.gwu.edu
vishal4790@gmail.com
vishal.bahedia@gwu.edu
vishal@visha.com
'''

print('\n matching email Id')
pattern = re.compile(r'[a-zA-z.0-9]+@[a-zA-z.]+(com|edu)')
matches = pattern.finditer(emails)
for match in matches:
	print(match)

urls = '''
https://www.google.com
http://youtube.com
https://www.corey.com
https://www.nasa.gov
'''
print('\nmatching urls')

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
	print(match.group(0))

print('subbed urls')
#pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.sub(r'\2\3',urls)
print(matches)
print(type(matches))


print('findall will only return the group')
print('\n matching names')
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*\s\w*')
matches = pattern.findall(text)
for match in matches:
	print(match)

	
print('match method will only search the start of the string')
pattern = re.compile(r'start')
matches = pattern.match(sentence)
print(matches)

print('search method will search the whole string')
pattern = re.compile(r'sentence')
matches = pattern.search(sentence)
print(matches)


print('re.IGNORECASE can be used to ignore the case')
pattern = re.compile(r'Start', re.IGNORECASE)
matches = pattern.search(sentence)
print(matches)