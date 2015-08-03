from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jobPostings/(?P<pk>[0-9]+)/$', views.customerListingDetail, name='customerListingDetail'),
    url(r'^tripPostings/(?P<pk>[0-9]+)/$', views.courierListingDetail, name='courierListingDetail'),
    url('^jobPosting/search/$', views.customerListingSearch, name='customerListingSearch'),
    url('^jobPosting/search/results$', JobSearchResults.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

