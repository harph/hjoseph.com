from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
    (r'^$', 'web.views.index'),
 	(r'^tweets/$', 'web.views.get_tweets'),
	(r'^posts/$', 'web.views.get_posts'),
	(r'^portafolio/(?P<project_name>.+)/$', 'web.views.get_portafolio_project'),
)
