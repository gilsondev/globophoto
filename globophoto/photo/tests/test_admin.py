# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib import admin as django_admin

from globophoto.photo.models import Photo
from globophoto.photo import admin


class PhotoAdmin(TestCase):
    def test_register(self):
        registry = django_admin.site._registry
        self.assertIn(Photo, registry)
