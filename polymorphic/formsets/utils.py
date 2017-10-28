"""
Internal utils
"""
from polymorphic.compat import DJANGO_GTE_2


def add_media(dest, media):
    """
    Optimized version of django.forms.Media.__add__() that doesn't create new objects.

    Only required for Django < 2.0
    """
    if DJANGO_GTE_2:
        dest += media
    else:
        dest.add_css(media._css)
        dest.add_js(media._js)
