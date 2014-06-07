# -*- coding: utf-8 -*-

from django.contrib import admin

from globophoto.photo.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    class Meta:
        model = Photo

admin.site.register(Photo, PhotoAdmin)
