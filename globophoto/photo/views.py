# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic import ListView

from globophoto.photo.models import Photo


class GalleryView(TemplateView):
    template_name = "photo/gallery.html"


class PhotoListView(ListView):
    model = Photo
