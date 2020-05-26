#timeTest.py
import datetime

print("can import datetime")
timeFormat = "%H:%M:%S"
print("now: " + str(datetime.datetime.now()))
print("time: " + datetime.datetime.now().strftime(myFormat))
#print("other time: " + datetime.strftime())