from django.conf.urls import patterns, include, url
from request import views as request_views

from . import views

app_name = 'request'

urlpatterns = [
#    url(r'^all/$', request_views.PERRequest),
    url(r'^all/$', 'request.views.requests'),
    url(r'^get/(?P<per_id>\d+)/$', 'request.views.request'),
]