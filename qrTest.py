import qrcode

img = qrcode.make('Insert dynamically generated qr code here')
#print(img)
img.save("data.png")
#https://pypi.org/project/qrcode/

#qr "text for qrcode" > qrcode.png

#this wasn't working until I changed this:
#/Users/dstrube/Library/Python/3.7/lib/python/site-packages
#to this:
#/usr/local/lib/python3.7/site-packages
#how did I find that path?
#pip show qrcode

#import sys

#print("sys.path: ")
#for x in sys.path:
#	print(x)
#print("sys.executable: " + sys.executable)
#print("sys.exec_prefix: " + sys.exec_prefix)
#print("sys.path_hooks: ") 
#for x in sys.path_hooks:
#	print(x)

