from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    name = 'oc_lettings_site'


class LettingsAppConfig(AppConfig):
    """Serve the letting app's name to settings.py"""
    name = 'lettings'