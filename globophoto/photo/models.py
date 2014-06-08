# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Photo(models.Model):
    """
    Model that represent photos in project.

    :param name: The name of photo
    :type name: str.
    :param image: The photo uploaded
    :type image: file.
    :param created_at: When image was created
    :type created_at: datetime
    """
    name = models.CharField(_(u"Nome da Imagem"), max_length=255)
    image = models.ImageField(_(u"Imagem"), upload_to="images", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    class Meta:
        db_table = 'photos'

    def __unicode__(self):
        return self.name

    @property
    def filename(self):
        """Parse file path to return filename"""
        return self.image.name.split('/')[-1]


from globophoto.photo import signals
