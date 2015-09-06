import os
import shlex 
import subprocess

def feedPip2nd(result):
	command_stdout01 = subprocess.Popen("FindingAffectedPipes.exe " + result, shell=True, stdout = subprocess.PIPE).stdout.read()
	command_text01 = command_stdout01.decode("utf-8")
	command_text01 = command_text01.split(" ")
	command_text01[-1] = command_text01[-1].strip("/r/n")
	
	return command_text01
	#command_text is unprocessed.