from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customerListing/$', views.CustomerListingList.as_view()),
    url(r'^customerListing/(?P<pk>[0-9]+)/$', views.CustomerListingDetail.as_view()),
    url('^search/(?P<startlocation>.+)/$', views.CustomerListingSearch.as_view()),
]