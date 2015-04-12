from django.conf.urls import patterns, include, url


urlpatterns = patterns('container.views',
    url(r'^$', 'container_list'),
)
