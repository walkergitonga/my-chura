from django.conf.urls import url, include
from django.contrib.auth.views import logout, login
from . import views

urlpatterns = [
	url(r'^$', views.register, name='register'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^restricted/$', views.restricted, name='restricted'),
]
