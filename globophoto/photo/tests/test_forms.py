# -*- coding: utf-8 -*-

import os

from django.test import TestCase
from django.core.files.images import ImageFile

from globophoto.photo.forms import PhotoForm
from globophoto.photo.models import Photo


class PhotoFormTest(TestCase):
    def setUp(self):
        file_name = 'image_test.jpg'
        image_path = os.path.dirname(__file__)
        image_file = open(os.path.join(image_path, file_name), 'r')
        data = {
            'image': ImageFile(image_file)
        }
        self.form = PhotoForm(files=data)
        assert self.form.is_valid()

    def test_create(self):
        photo = self.form.save()
        self.assertTrue(photo.pk)
