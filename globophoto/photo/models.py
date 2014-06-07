# -*- coding: utf-8 -*-

from django.db import models


class Photo(models.Model):
    image = models.FileField(upload_to="images", max_length=255)
