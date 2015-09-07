import os
import shlex 
import subprocess
from FindingPath import *

def feedPipe2(coordinates):
	working = os.getcwd() + "/stormwatermonitor/helpers/"
	points = working + "points.csv"
	segments = working + "segments.csv"
	#a relative path problem original script as bellow, runs okay when tested with python within helpers/
	'''
	points = "points.csv"
	segments = "segments.csv"
	'''
	
	(x, y) = coordinates
	findingPathObj = FindingPath(points, segments)
	#aPoint = findingPath.findNearestPoint(x, y)
	#path = findingPath.findingDownstream(aPoint)
	path = findingPathObj.findingDownstream(float(x), float(y))
	return path.split(" ")
	
	
	
#===============original method of feeding pipe with subprocess calling executable. 
'''
Due to the previllage reason, we are experiencing issue with calling executable. 
Thus using feedPipe2
'''
def feedPipe(coordinates):
	working = os.getcwd() + "/stormwatermonitor/helpers/"
	#command_stdout = subprocess.Popen("FindingPath.exe " + coordinates, shell=True, stdin = subprocess.PIPE, stderr = subprocess.PIPE, stdout = subprocess.PIPE, cwd=working).stdout.read()
	command_stdout = subprocess.Popen(working+"FindingPath.exe " + coordinates, shell=True, stdin = subprocess.PIPE, stderr = subprocess.PIPE, stdout = subprocess.PIPE).stdout.read()
	#print(type(command_stdout))
	command_text = command_stdout.decode("utf-8")
	#preprocess the string
	command_text = command_text.split(" ")
	command_text[-1] = command_text[-1].strip("/r/n")
	return command_text
	#==============================================
