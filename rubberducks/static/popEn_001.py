import os
import shlex 
import subprocess

def feedPip(coordinates):
	command_stdout = subprocess.Popen("FindingNearestPipe.exe " + coordinates, shell=True, stdout = subprocess.PIPE).stdout.read()
	#print(type(command_stdout))
	command_text = command_stdout.decode("utf-8")
	#preprocess the string
	command_text = command_text.split(" ")
	command_text[-1] = command_text[-1].strip("/r/n")
	result = command_text[-1]
	return feedPip2nd(result)
	#==============================================
def feedPip2nd(result):
	command_stdout01 = subprocess.Popen("FindingAffectedPipes.exe " + result, shell=True, stdout = subprocess.PIPE).stdout.read()
	command_text01 = command_stdout01.decode("utf-8")
	command_text01 = command_text01.split(" ")
	command_text01[-1] = command_text01[-1].strip("/r/n")
	
	return command_text01
	#command_text is unprocessed.