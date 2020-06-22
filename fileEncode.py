#fileEncode.py

#Take in a file, output it as base64 encoded? or octet stream?
#for this:
#https://docs.brightsign.biz/display/DOC/Remote+DWS#RemoteDWS-/files/{:path}

import base64
#import codecs
#https://docs.python.org/3/library/codecs.html#binary-transforms
#https://docs.python.org/3/library/base64.html#base64.encodebytes
import os

filePath = "test.txt"

print("file length: "+str(os.stat(filePath).st_size))

#1: read in as plain text
print("original file contents: ")
with open(filePath, "rt") as fileIn:
	for lineIn in fileIn:
		#print("in loop:")
		print(lineIn.strip())
		#print("binary: ")
		#print(lineIn.strip().encode())

"""#if we want to loop thru the file after readlines (or vice versa), 
#must be in another 'with' clause
with open(filePath, "rt") as fileIn:
	lines = fileIn.readlines()
	print("all lines (list):")
	print(lines) 

#read in all text file as binary
with open(filePath, "rb") as fileIn:
	lines = fileIn.readlines()
	print("read all in as binary (list):")
	print(lines)

#loop thru a text file as binary?
with open(filePath, "rb") as fileIn:
	print("read in as binary in a loop:")
	for lineIn in fileIn:
		print(lineIn)
"""
#read in a text file as binary of given size
with open(filePath, "rb") as fileIn:
	lines = fileIn.read(os.stat(filePath).st_size)
	print("read all in as binary of given size:")
	print(lines)
	print("encoded: ")
	encoded = base64.b64encode(lines)
	print(encoded)

print("encoded outside with:")
print(encoded)

print("decoded:")
print(base64.decodebytes(encoded))

#with codecs.open(filePath,'rb',encoding='utf-8',errors='ignore') as fileIn:
#	print("encoded 1 way: ")
#	for lineIn in fileIn:
#		#b64encode takes in bytes, not a string
#		encoded1 = base64.b64encode(lineIn.encode())
#		print(encoded1)
#print("another way:")
#encoded2 = base64.b64encode(b'this is a test\nline2') #content of the file
#print(encoded2)

#example of encode with funky char:
#txt = "My name is Ståle"
#x = txt.encode()
#print(x)
