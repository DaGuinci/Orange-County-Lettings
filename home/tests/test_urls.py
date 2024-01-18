from django.test import TestCase, Client
from django.urls import reverse


class TestUrls(TestCase):
    """
    Class testcase pour les urls
    """
    client = Client()

    def test_home_url_is_resolved(self):
        """
        Test du fonctionnement du namespace home et de la fonction index
        """
        url = reverse('home:index')
        assert url == '/'
