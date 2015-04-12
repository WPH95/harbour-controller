from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'harbout_agent.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'image.views.image_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^container/', include('container.urls')),
    url(r'^image/', include('image.urls')),
)
