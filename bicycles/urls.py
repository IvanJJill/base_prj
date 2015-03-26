from django.conf.urls import patterns, include, url
from bicycles import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<bike_id>\d+)/$', views.bike_details, name='bikes'),
                       url(r'^orders(?P<order_id>\d+)/$', views.order_details, name='orders'),
                       )