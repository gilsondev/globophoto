# -*- coding: utf-8 -*-

from django.db import models


class Photo(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images", max_length=255)

    class Meta:
        db_table = 'photos'

    @property
    def filename(self):
        return self.image.name.split('/')[-1]


from globophoto.photo import signals
