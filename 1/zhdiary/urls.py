from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('zh_RSS.urls', namespace='zh_RSS')),
    # Examples: 
    # url(r'^$', 'zhdiary.views.home', name='home'),
    # url(r'^zhdiary/', include('zhdiary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
     ('^/(?P<path>.*)','django.views.static.serve',{'document_root': settings.STATIC_PATH}),   
)
