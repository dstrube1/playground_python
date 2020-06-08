#challenge7
#https://www.linkedin.com/learning/python-code-challenges/set-an-alarm?u=2163426

#Set an alarm
#function to play a sound and print a message at a set time

"""Research:
#import vlc
#https://wiki.videolan.org/Python_bindings
	#p = vlc.MediaPlayer(soundFile)
	#p.play()
#doesn't crash, but doesn't seem to work

#from playsound import playsound
#No module named 'AppKit'
#->
#pip install AppKit 
#-> [big long error]
	#playsound(soundFile)

#import winsound
#Could not find a version that satisfies the requirement winsound

#other options:
#https://stackoverflow.com/questions/20021457/playing-mp3-song-on-python#25899180
"""

import os

import sched
import time

def setAlarm(alarmTime, soundFile, message_):
	s = sched.scheduler(time.time, time.sleep)
	s.enterabs(alarmTime, 1, print, argument=(message_,))
	#s.enterabs(alarmTime, 1, os.system, argument=("afplay " + soundFile),) 
	#^using os.system as the function is - to put it mildly - tricky; best to call my own:
	s.enterabs(alarmTime, 1, playsound, argument=(soundFile,))
	print("Alarm set for", time.asctime(time.localtime(alarmTime)))
	s.run()

def playsound(soundFile):
	os.system("afplay " + soundFile) 
	#"use of os.system is strongly discouraged. Use subprocess instead or even sh if you must"
	#^good advice for big project, not this
	
#main:
#do it one second from now
#challenge7.mp3 : Jake Chudnow - 145 (Poodles)
setAlarm(time.time()+1, "challenge7.mp3", "Wake up") 
	
