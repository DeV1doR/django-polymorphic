try:
    # Django 2.0+
    from django.urls import URLResolver
except ImportError:
    # Django < 2.0
    from django.urls import RegexURLResolver as URLResolver
