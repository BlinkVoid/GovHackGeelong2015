import csv

def mapPipelines():
	with open('points.csv') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar= '|')
		print (reader)
		pipelineNetwork = []
		for row in reader:
			pipelineNetwork += row
		# print (len(pipelineNetwork))
		# print (pipelineNetwork)
	return pipelineNetwork