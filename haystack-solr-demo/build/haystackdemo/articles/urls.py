from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('articles.views',
    url(r'^(?P<slug>[-\w]+)/$', 'detail', name='articles_detail'),
)
