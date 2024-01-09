from django.test import TestCase, Client
import pytest


class TestViews(TestCase):
    client = Client()

    def test_index_is_online(self):
        response = self.client.get('/')
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'home/index.html')

    def test_page_404(self):
        response = self.client.get('/lettings/0/')
        assert response.status_code == 404
        self.assertTemplateUsed(response, 'home/404.html')

    def test_page_500(self):
        with pytest.raises(Exception):
            response = self.client.get('/error')

            assert response.status_code == 500
            self.assertTemplateUsed(response, 'home/500.html')
