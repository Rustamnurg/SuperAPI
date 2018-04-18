from django.conf.urls import url

from blog import api
from . import views

urlpatterns = [
    url(r'^api/report/', api.post_list, name='report'),
    url(r'^result/', views.current_datetime, name='result'),
    url(r'^signIn/', views.signIn, name='signIn'),
    url(r'^signUp/', views.signUp, name='signUp'),
    url(r'^logout/', views.logout, name='logout'),



]