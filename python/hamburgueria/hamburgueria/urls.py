from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('hamburgueria.views',
                       
    url(r'^admin/', include(admin.site.urls)),
    url(r'^snippets/$', 'snippet'),
    url(r'^snippets$', 'snippet'),
    url(r'^snippets/(?P<pk>[0-9]+)$', 'snippet_detail'),

)
