from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'tricklelist.views.index'),
)

