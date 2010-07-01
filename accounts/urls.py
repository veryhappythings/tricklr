(r'^accounts/login/$', 'django.contrib.auth.views.login'),


from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout'),
    (r'^profile/$', 'accounts.views.user_detail'),
    (r'^profile/(?P<user_id>\d+)$', 'accounts.views.user_detail'),
)
