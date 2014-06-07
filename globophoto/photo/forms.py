# -*- coding: utf-8 -*-

from django import forms

from globophoto.photo.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        exclude = ('name',)
        model = Photo
