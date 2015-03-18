from django.conf.urls import patterns, include, url
from django.contrib import admin
import bicycles

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'base_prj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', 'base_prj.views.home', name='home'),
    url(r'^bikes/', include(bicycles.urls), name='bikes'),
    url(r'^admin/', include(admin.site.urls)),

)
