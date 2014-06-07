# -*- coding: utf-8 -*-

from django import forms

from globophoto.photo.models import Photo


class PhotoForm(forms.ModelForm):
    """Form used to insert photos"""
    class Meta:
        model = Photo
        exclude = ['name']
