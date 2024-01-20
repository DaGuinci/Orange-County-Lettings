from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


class TestUrls(TestCase):
    """
    Class testcase pour les urls
    """
    client = Client()

    @classmethod
    def setUpTestData(cls):
        user_test = User.objects.create(
            username='user_test',
            email='user@test.com'
        )
        cls.profile = Profile.objects.create(
            user=user_test,
            favorite_city='test_city'
        )

    def test_profiles_list_url_is_resolved(self):
        """
        Test du fonctionnement du namespace profiles et de la fonction index
        """
        url = reverse('profiles:index')
        assert url == '/profiles/'

    def test_profile_url_is_resolved(self):
        """
        Test du fonctionnement du namespace profiles et de la fonction profile
        """
        url = reverse('profiles:profile', kwargs={'username': self.profile.user.username})
        assert url == '/profiles/'+str(self.profile.user.username)+'/'
