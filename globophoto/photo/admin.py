# -*- coding: utf-8 -*-

from django.contrib import admin

from globophoto.photo.models import Photo
from globophoto.photo.forms import PhotoForm


class PhotoAdmin(admin.ModelAdmin):
    form = PhotoForm

    class Meta:
        model = Photo

admin.site.register(Photo, PhotoAdmin)
