from django.test import TestCase, Client


class TestViews(TestCase):
    """
    Class testcase pour les views
    """

    client = Client()

    def test_index_is_online(self):
        """
        Test le retour de l'adresse '/':
        La page index s'affiche.
        """
        response = self.client.get('/')
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'home/index.html')

    def test_page_404(self):
        """
        Test le retour d'une adresse erronée:
        La page 404 personnalisée s'affiche.
        """
        response = self.client.get('/lettings/0/')
        assert response.status_code == 404
        self.assertTemplateUsed(response, 'home/404.html')

    def test_page_500(self):
        """
        Test le retour de l'adresse '/error', qui lance la fonction
        error_generating de home/view.py:
        La page 500 personnalisée s'affiche.
        """
        response = self.client.get('/error')
        assert response.status_code == 500
        self.assertTemplateUsed(response, 'home/500.html')
