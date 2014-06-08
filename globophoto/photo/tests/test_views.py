# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from globophoto.photo.tests.utils import images
from globophoto.photo.models import Photo


class GalleryView(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('photo:home'))

    def test_get(self):
        """GET / should return status code 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Should render template photo/gallery.html"""
        self.assertTemplateUsed(self.resp, "photo/gallery.html")


class PhotoListView(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('photo:list'))

    def test_get(self):
        """GET /photos/ should return status code 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Should render template photo/photo_list.html"""
        self.assertTemplateUsed(self.resp, "photo/photo_list.html")


class PhotoCreateView(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('photo:create'))

    def test_get(self):
        """GET /photos/new/ should return status code 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Should render template photo/photo_form.html"""
        self.assertTemplateUsed(self.resp, "photo/photo_form.html")


class PhotoUpdateView(TestCase):
    def setUp(self):
        data = {
            'image': images.load_image()
        }
        photo = Photo.objects.create(**data)
        self.resp = self.client.get(reverse('photo:update',
                                            kwargs={'pk': photo.pk}))

    def test_get(self):
        """GET /photos/update/ should return status code 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Should render template photo/photo_form.html"""
        self.assertTemplateUsed(self.resp, "photo/photo_form.html")
