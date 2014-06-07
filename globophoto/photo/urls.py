from django.conf.urls import patterns, url

from globophoto.photo.views import GalleryView

urlpatterns = patterns(
    '',
    url(r'$', GalleryView.as_view(), name='home'),
)
