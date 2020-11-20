#bsa/urls.py
from django.urls import path

from . import views

app_name = 'bsa'
urlpatterns = [
	path('', views.index, name='index'),
	# ex: /bsa/5/
	path('<int:device_id>/', views.getInfo, name='getInfo'),
	# ex: /bsa/5/snapshot/
	path('<int:device_id>/snapshot/', views.getSnapshot, name='snapshot'),
	# ex: /bsa/5/reboot/
	path('<int:device_id>/reboot/', views.reboot, name='reboot'),
]