# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView


class GalleryView(TemplateView):
    template_name = "photo/gallery.html"
