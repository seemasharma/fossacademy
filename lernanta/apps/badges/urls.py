from django.conf.urls.defaults import patterns, url, include


urlpatterns = patterns('',
  (r'^obi/', include('django_obi.urls')),
  url(r'^create/$', 'badges.views.create',
      name='badges_create'),
  url(r'^(?P<slug>[\w-]+)/$', 'badges.views.show',
      name='badges_show'),
  url(r'^(?P<slug>[\w-]+)/$', 'badges.views.badge_description',
      name='badge_description'),
  url(r'^(?P<slug>[\w-]+)/award/create/$', 'badges.views.create_submission',
      name='submission_create'),
  url(r'^award/(?P<submission_id>\d+)/$',
      'badges.views.show_submission',
      name='submission_show'),

)
