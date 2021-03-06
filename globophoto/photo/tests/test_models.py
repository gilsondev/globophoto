# -*- coding: utf-8 -*-

from django.test import TestCase

from globophoto.photo.tests.utils import images
from globophoto.photo.models import Photo


class PhotoTest(TestCase):
    def setUp(self):
        self.fields = Photo._meta.get_all_field_names()

    def test_should_file_field(self):
        """Should have file field in model"""
        self.assertIn("image", self.fields)

    def test_should_name_field(self):
        """Should have name field in model"""
        self.assertIn("name", self.fields)

    def test_create(self):
        """Should create the photo object"""
        data = {
            'image': images.load_image()
        }
        photo = Photo.objects.create(**data)
        self.assertTrue(photo.pk)
