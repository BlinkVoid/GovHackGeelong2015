import os
import shlex 
import subprocess

def feedPip(coordinates):
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
