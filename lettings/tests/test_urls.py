from django.test import TestCase, Client
from django.urls import reverse
from lettings.models import Letting
from lettings.models import Address


class TestUrls(TestCase):
    """
    Class testcase pour les urls
    """
    client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            number=123,
            zip_code=12345
        )
        cls.letting = Letting.objects.create(
            title='Letting_name',
            address_id=cls.address.id
        )

    def test_lettings_list_url_is_resolved(self):
        """
        Test du fonctionnement du namespace lettings et de la fonction index
        """
        url = reverse('lettings:index')
        assert url == '/lettings/'

    def test_letting_url_is_resolved(self):
        """
        Test du fonctionnement du namespace lettings et de la fonction letting
        """
        url = reverse('lettings:letting', kwargs={'letting_id': self.letting.id})
        assert url == '/lettings/'+str(self.letting.id)+'/'
