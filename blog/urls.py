from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/report/', views.post_list, name='report'),
]