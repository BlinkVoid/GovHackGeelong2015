import csv

with open('points.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar= '|')
	print (reader)
	pipelineNetwork = []
	for row in reader:
		print(type(row), row)