# -*- coding: utf-8 -*-

from django.db.models.signals import pre_save
from django.dispatch import receiver

from globophoto.photo.models import Photo


# TODO: Need test
@receiver(pre_save, sender=Photo)
def generate_name(sender, instance, **kwargs):
    """
    Capture the filename and set to name field
    """
    instance.name = instance.filename
