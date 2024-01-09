from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User


# models test
class ProfilesModelsTest(TestCase):

    def test_profile_creation(self):
        user_test = User.objects.create(
            username='user_test',
            email='user@test.com'
        )
        profile_test = Profile.objects.create(
            user=user_test,
            favorite_city='test_city'
        )
        self.assertTrue(isinstance(profile_test, Profile))
        assert str(profile_test) == 'user_test'
