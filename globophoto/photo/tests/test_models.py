# -*- coding: utf-8 -*-

import os

from django.test import TestCase
from django.core.files.images import ImageFile

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
        file_name = 'image_test.jpg'
        image_path = os.path.dirname(__file__)
        image_file = open(os.path.join(image_path, file_name), 'r')
        data = {
            'image': ImageFile(image_file)
        }
        photo = Photo.objects.create(**data)
        self.assertEqual(photo.pk, 1)
        self.assertEqual(photo.name, file_name)

