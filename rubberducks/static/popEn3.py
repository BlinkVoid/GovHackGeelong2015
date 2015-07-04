import os
import shlex 
import subprocess

def feedPip(coordinates):
	command_stdout = subprocess.Popen("FindingPath.exe " + coordinates, shell=True, stdout = subprocess.PIPE).stdout.read()
	#print(type(command_stdout))
	command_text = command_stdout.decode("utf-8")
	#preprocess the string
	command_text = command_text.split(" ")
	command_text[-1] = command_text[-1].strip("/r/n")
	return command_text
	#==============================================
