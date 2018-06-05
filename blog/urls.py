from django.conf.urls import url

from blog import api
from . import views

urlpatterns = [
    url(r'^api/report/', api.report, name='report'),
    url(r'^result/', views.current_datetime, name='result'),
    url(r'^my/', views.my, name='my'),
    url(r'^signIn/', views.signIn, name='signIn'),
    url(r'^signUp/', views.signUp, name='signUp'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^enterAppName/', views.enterAppName, name='enterAppName'),




]