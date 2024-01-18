from django.test import TestCase, Client
from profiles.models import Profile
from django.contrib.auth.models import User


class TestViews(TestCase):
    """
    Class testcase pour les views
    """

    client = Client()

    @classmethod
    def setUpTestData(cls):
        """
        Créer les ressources (user et profile) nécessaires à la suite
        de tests
        """
        user_test = User.objects.create(
            username='user_test',
            email='user@test.com'
        )
        cls.profile = Profile.objects.create(
            user=user_test,
            favorite_city='test_city'
        )

    def test_get_profiles_list(self):
        """
        Test de l'affichage de la page index des profiles
        """
        response = self.client.get('/profiles/')
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_get_profile_detail(self):
        """
        Test de l'affichage de la page détaillée d'un profile
        """
        response = self.client.get('/profiles/'+str(self.profile.user.username)+'/')
        assert response.status_code == 200
        self.assertContains(response, self.profile.user.username)
        self.assertTemplateUsed(response, 'profiles/profile.html')
