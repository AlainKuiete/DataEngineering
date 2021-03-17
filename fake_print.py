import csv

with open('data.CSV') as f:
	myreader=csv.DictReader(f)
	headers=next(myreader)
	print(headers)
	for row in myreader:
		print(row['name'], ' | ', row['city'])
