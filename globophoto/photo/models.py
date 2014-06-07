# -*- coding: utf-8 -*-

from django.db import models


class Photo(models.Model):
    """
    Model that represent photos in project.

    :param name: The name of photo
    :type name: str.
    :param image: The photo uploaded
    :type image: file.
    """
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images", max_length=255)

    class Meta:
        db_table = 'photos'

    def __unicode__(self):
        return self.name

    @property
    def filename(self):
        """Parse file path to return filename"""
        return self.image.name.split('/')[-1]


from globophoto.photo import signals
