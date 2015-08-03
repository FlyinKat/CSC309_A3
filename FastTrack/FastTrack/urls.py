"""FastTrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from home import views
from ft.views import *

urlpatterns = [
    url(r'^api/', include('ft.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'ft.views.home', name='home'),
    url(r'^$', 'home.views.index'),
    
    url(r'^login/$', 'FastTrack.views.login'),
    url(r'^logout/$', 'FastTrack.views.logout'),
    url(r'^auth/$', 'FastTrack.views.auth_view'),
    url(r'^loggedin/$', 'FastTrack.views.loggedin'),
    url(r'^home/$', 'FastTrack.views.home'),
    url(r'^invalid/$', 'FastTrack.views.invalid_login'),
    url(r'^register/$', 'FastTrack.views.register_user'),
    url(r'^register_success/$', 'FastTrack.views.register_success'),
    url(r'^search_jobs/$', 'ft.views.customerListingSearch', name='customerListingSearch'),
    url(r'^search_jobs/results$', JobSearchResults.as_view()),
    url(r'^search_trips/$', 'FastTrack.views.search_trips'),
    url(r'^post_jobs/$', 'ft.views.createCustomerListing' , name='createCustomerListing'),
    url(r'^post_trips/$', 'ft.views.createCourierListing' , name='createCourierListing' ),
    url(r'^profile/$', 'FastTrack.views.Profile'),
    url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url('', include('social_auth.urls')),

]
