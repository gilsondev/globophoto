# -*- coding: utf-8 -*-

from django.test import TestCase

from globophoto.photo.models import Photo


class PhotoTest(TestCase):
    def test_should_file_field(self):
        """Should have file field in model"""
        fields = Photo._meta.get_all_field_names()
        self.assertIn("image", fields)
