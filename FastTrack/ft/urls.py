from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customerListing/$', views.CustomerListingList.as_view()),
    url(r'^customerListing/(?P<pk>[0-9]+)/$', views.CustomerListingDetail.as_view()),
    url('^search/(?P<startlocation>.+)/$', views.CustomerListingSearch.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
