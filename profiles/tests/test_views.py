from django.test import TestCase, Client
from profiles.models import Profile
from django.contrib.auth.models import User


class TestViews(TestCase):
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

    def test_get_profiles_list(self):
        response = self.client.get('/profiles/')
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_get_profile_detail(self):
        response = self.client.get('/profiles/'+str(self.profile.user.username)+'/')
        assert response.status_code == 200
        self.assertContains(response, self.profile.user.username)
        self.assertTemplateUsed(response, 'profiles/profile.html')
