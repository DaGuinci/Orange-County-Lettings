from django.test import TestCase, Client
from lettings.models import Letting
from lettings.models import Address


class TestViews(TestCase):
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

    def test_get_lettings_list(self):
        response = self.client.get('/lettings/')
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_get_letting_detail(self):
        response = self.client.get('/lettings/'+str(self.letting.id)+'/')
        assert response.status_code == 200
        self.assertContains(response, 'Letting_name')
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_wrong_letting_page_gives_404(self):
        response = self.client.get('/lettings/'+str(self.letting.id-1)+'/')
        assert response.status_code == 404
