from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^userprofile/$', 'userprofile.views.user_profile'),
                       )