#htmlread.py
#https://www.instructables.com/HTML-to-Python/
#fails at php's call to out.php
from time import sleep

def read():
	inlist = ['A','B','C']
	while True:
		file=open("formdata.txt","r")
		data = file.read()
		for i in range(len(inlist)):
			if data == inlist[i]:
				print(data)
				file=open("formdata.txt","w")
				file.write("")
		file.close()
		sleep(0.01)
		
		
read()