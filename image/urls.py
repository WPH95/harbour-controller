from django.conf.urls import patterns, include, url


urlpatterns = patterns('image.views',
    url(r'^$', 'image_list'),
)
