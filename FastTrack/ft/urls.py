from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jobPostings/(?P<pk>[0-9]+)/$', views.CustomerListingDetail.as_view()),
    url(r'^tripPostings/(?P<pk>[0-9]+)/$', views.CourierListingDetail.as_view()),
    url('^jobPosting/search/$', views.customerListingSearch, name='customerListingSearch'),
    url('^jobPosting/search/results$', views.customerListingSearchResults, name='customerListingSearchResults'),
    url(r'^jobPostings/create$', views.createCustomerListing , name='createCustomerListing' ),
    url(r'^tripPostings/create$', views.createCourierListing , name='createCourierListing' ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

