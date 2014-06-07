# -*- coding: utf-8 -*-

from django.test import TestCase

from globophoto.photo.tests.utils import images
from globophoto.photo.forms import PhotoForm


class PhotoFormTest(TestCase):
    def setUp(self):
        data = {
            'image': images.load_image()
        }
        self.form = PhotoForm(files=data)
        assert self.form.is_valid()

    def test_create(self):
        """Should create photo with modelform"""
        photo = self.form.save()
        self.assertTrue(photo.pk)
