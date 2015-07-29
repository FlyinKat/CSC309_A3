from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^listing/$', views.ListingList.as_view()),
    url(r'^listing/(?P<pk>[0-9]+)/$', views.ListingDetail.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)