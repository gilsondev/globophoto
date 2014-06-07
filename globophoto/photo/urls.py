from django.conf.urls import patterns, url

from globophoto.photo.views import (
    GalleryView, PhotoListView, PhotoCreateView
)

urlpatterns = patterns(
    '',
    url(r'^$', GalleryView.as_view(), name='home'),
    url(r'^photos/$', PhotoListView.as_view(), name='list'),
    url(r'^photos/new/$', PhotoCreateView.as_view(), name='create'),
)
