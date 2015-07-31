from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customerListing/$', views.CustomerListingList.as_view()),
    url(r'^jobPostings/(?P<pk>[0-9]+)/$', views.CustomerListingDetail.as_view()),
    url(r'^courierPostings/(?P<pk>[0-9]+)/$', views.CourierListingDetail.as_view()),
    url('^search/(?P<startlocation>.+)/$', views.CustomerListingSearch.as_view()),
    url(r'^customerListing/create$', views.createCustomerListing , name='createCustomerListing' ),
    url(r'^courierListing/create$', views.createCourierListing , name='createCourierListing' ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

