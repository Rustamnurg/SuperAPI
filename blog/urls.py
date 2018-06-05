from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

from blog import api
# from mysite import settings
from . import views
import os

urlpatterns = [
    url(r'^api/report/', api.report, name='report'),
    url(r'^result/', views.current_datetime, name='result'),
    url(r'^my/', views.my, name='my'),
    url(r'^signIn/', views.signIn, name='signIn'),
    url(r'^signUp/', views.signUp, name='signUp'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^enterAppName/', views.enterAppName, name='enterAppName'),
    # url('',(r'^images/(?P<path>.*)$', 'django.views.static.serve',
    #              {'document_root': "/images/"}),
    #           ),
    # url('',
    #            (r'^images/(?P<path>.*)$', 'django.views.static.serve',
    #              {'document_root': ""}),
    #           )
    # (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'images': settings.MEDIA_ROOT}),
    url(r'^media/(.*)$', serve, {'document_root':os.path.join(os.path.dirname(__file__), 'images')}),




]