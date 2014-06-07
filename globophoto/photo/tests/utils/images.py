# -*- coding: utf-8 -*-

import os

from django.core.files.images import ImageFile


def load_image(path=None):
    """
    Load image and return ImageFile object

    :param path: Path of image
    :type path: str.
    """
    if not path:
        base_dir = os.path.dirname(__file__)
        path = os.path.join(base_dir, 'image_test.jpg')

        image = ImageFile(open(path, 'r'))
    return image
