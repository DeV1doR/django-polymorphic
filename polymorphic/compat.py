import django

DJANGO_GTE_2 = django.VERSION >= (2, 0)

try:
    # Django 2.0+
    from django.urls import URLResolver
except ImportError:
    # Django < 2.0
    from django.urls import RegexURLResolver as URLResolver
