from django.conf.urls.defaults import *



urlpatterns = patterns('',
    url(r'^$','trackit.views.show_charts'),

)