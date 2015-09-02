from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', hello.views.index, name='index'),
    #url(r'^db', hello.views.db, name='db'),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_export/', include("admin_export.urls", namespace="admin_export")),

)
