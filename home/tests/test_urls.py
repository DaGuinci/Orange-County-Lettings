from django.test import TestCase, Client
from django.urls import reverse


class TestUrls(TestCase):
    client = Client()

    def test_home_url_is_resolved(self):
        url = reverse('home:index')
        assert url == '/'
