# -*- coding: utf-8 -*-

from django.test import TestCase


class GalleryView(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """GET / should return status code 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Should render template photo/gallery.html"""
        self.assertTemplateUsed(self.resp, "photo/gallery.html")


class PhotoListView(TestCase):
    def setUp(self):
        self.resp = self.client.get('/photos/')

    def test_get(self):
        """GET /photos/ should return status code 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Should render template photo/photo_list.html"""
        self.assertTemplateUsed(self.resp, "photo/photo_list.html")
