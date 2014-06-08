# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from globophoto.photo.models import Photo
from globophoto.photo.forms import PhotoForm


class GalleryView(TemplateView):
    template_name = "photo/gallery.html"


class PhotoListView(ListView):
    model = Photo


class PhotoCreateView(CreateView):
    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('photo:list')


class PhotoUpdateView(UpdateView):
    template_name = "photo/photo_form.html"
    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('photo:list')


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:list')
