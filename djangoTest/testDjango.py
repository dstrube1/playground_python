#testDjango.py
import django

#https://docs.djangoproject.com/en/3.0/intro/tutorial01/

print("Can import django")
print("version: " + django.get_version())
#2020-07-10: 3.0.6

"""
plan:
0- verify installed (on mac: 3.1.2):
django-admin version

1- make & run django site on web dev
django-admin startproject brightsignAdmin
	in brightsignAdmin/urls.py:
	add: 
		getInfo
		reboot
		getSnapshot
		updateFirmware
	remove: others

a- start server (foreach python, use python3):
python manage.py runserver --noreload --nothreading
#specify port:
#python manage.py runserver 8080
#specify IP address and port:
#python manage.py runserver 10.138.28.37:8000
#run in background and return to command prompt
#python manage.py runserver &

b- create app (project contains multiple apps):
python manage.py startapp bsa

c- create app urls.py:
bsa/urls.py

d- add reference to bsa/urls.py to brightsignAdmin/urls.py
	add index to bsa/views.py

e- migrate:
python manage.py migrate

f- populate models.py in bsa 

g- update settings.py with reference to bsa

h- run these:
python manage.py makemigrations bsa
python manage.py check
python manage.py migrate
python manage.py inspectdb
python manage.py createsuperuser --username dstrube --email dstrube3@gatech.edu

python manage.py createsuperuser --username dstrube --email affamato@gmail.com
[local pw = 1
can ignore validators]

i- update bsa/admin.py to allow admin to add and edit devices

j- add to bsa/views.py: def getInfo... etc
	add to bsa/urls.py: references to views

python manage.py runserver --noreload --nothreading


2- prove can access site on web dev from web dev's html home
from index.html: link to something lke:
brightsignAdmin:8000

3- make function in django site to get info from a device in office
	brightsignUtil.py
	getInfo (maybe output to file and then update db with file contents?)

4- prove can access function on web dev from web dev's html home
5- make login page outside django
6- make all the functions
7- with db debug turned off, make database with all the device info:
	device name, uptime, version #s, assets page URL, serial #, IP address
"""