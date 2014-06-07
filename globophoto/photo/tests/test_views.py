# -*- coding: utf-8 -*-

from django.test import TestCase


class GalleryView(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """GET / should return status code 200"""
        self.assertEqual(self.resp.status_code, 200)
