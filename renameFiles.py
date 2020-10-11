#renameFiles.py
#Take all files in a directory, rename them numerically

import os

#TODOs: 
#1- add command line parameter for input path
#2- add logic to detect all file types- if they're all the same, no need to specify it in code
#3- add detection for order of magnitude of number of files 
#	(e.g., if less than 100, O = 10.)
#	prefix file names with 0s accordingly

my_path = "/Users/dstrube/Desktop/Temp/"
(_, _, file_names) = next(os.walk(my_path))

i = 1
for fn in sorted(file_names):
	new_name = ""
	if i < 10:
		new_name = "0"
	new_name += str(i) + ".png"
	print(fn + " -> " + my_path+new_name)
	i += 1
	os.rename(my_path+fn, my_path+new_name)