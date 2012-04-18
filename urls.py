from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

    url(r'^$','metrics.views.home'),
    url(r'^add/$', 'metrics.views.add'),
    url(r'^(?P<team_name>[a-zA-Z0-9_]*?)/$', 'metrics.views.team'),
    url(r'^(?P<team_name>[a-zA-Z0-9_]*?)/(?P<ye1>[0-9]{4})/$','metrics.views.team' ), 
    url(r'^(?P<team_name>[a-zA-Z0-9_]*?)/(?P<ye1>[0-9]{4})-(?P<ye2>[0-9]{4})/$','metrics.views.team'),
    url(r'openlogo-50.png','metrics.views.image', {'add':'openlogo-50.png'}),
    url(r'gradient.png','metrics.views.image', {'add':'gradient.png'}),
    url(r'[a-zA-Z0-9]*?/res.png$','metrics.views.image', {'add':'res.png'}),
)
