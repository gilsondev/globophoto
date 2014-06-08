from django.conf.urls import patterns, url

from globophoto.photo.views import (
    GalleryView, PhotoListView, PhotoCreateView,
    PhotoUpdateView
)

urlpatterns = patterns(
    '',
    url(r'^$', GalleryView.as_view(), name='home'),
    url(r'^photos/$', PhotoListView.as_view(), name='list'),
    url(r'^photos/new/$', PhotoCreateView.as_view(), name='create'),
    url(r'^photos/update/(?P<pk>[\d]+)/$', PhotoUpdateView.as_view(),
        name='update'),
)
