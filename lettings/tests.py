from django.test import TestCase
from django.urls import resolve, reverse
from lettings.models import Letting
from lettings.models import Address


class TestUrls(TestCase):

    def test_lettings_list_url(self):
        url = reverse('lettings')
        print(url)