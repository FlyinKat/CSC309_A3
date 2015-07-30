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

urlpatterns = [
    url(r'^api/', include('ft.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'ft.views.home', name='home'),
    url(r'^$', 'home.views.index'),
    
    url(r'^login/$', 'FastTrack.views.login'),
    url(r'^logout/$', 'FastTrack.views.logout'),
    url(r'^auth/$', 'FastTrack.views.auth_view'),
    url(r'^loggedin/$', 'FastTrack.views.loggedin'),
    url(r'^invalid/$', 'FastTrack.views.invalid_login'),
    url(r'^register/$', 'FastTrack.views.register_user'),
    url(r'^register_success/$', 'FastTrack.views.register_success'),
]
