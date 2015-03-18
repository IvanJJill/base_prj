from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^/all', 'base_prj.views.bicycles' ),
                       url(r'^/(?P<bicycle_id>\d+)/$', 'base_prj.views.bicycle'),
                       )