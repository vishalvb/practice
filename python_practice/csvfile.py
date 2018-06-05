#working with csv file operations
import csv

with open('survey_data.csv','r') as f:
	csv0 = csv.reader(f)
	
	for line in csv0:
		print(line)
		
print('using dictreader')

with open('survey_data.csv','r') as f:
	csv1 = csv.DictReader(f)
	
	for line in csv1:
		print(line)