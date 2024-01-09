from django.test import TestCase
from lettings.models import Address, Letting


# models test
class LettingsModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.address_test = Address.objects.create(
            number=123,
            street='Test Street',
            zip_code=12345
        )
        cls.letting_test = Letting.objects.create(
            title='Letting_test_name',
            address_id=cls.address_test.id
        )

    def test_address_creation(self):
        assert str(self.address_test) == '123 Test Street'
        self.assertTrue(isinstance(self.address_test, Address))

    def test_letting_creation(self):
        self.assertTrue(isinstance(self.letting_test, Letting))
        assert str(self.letting_test) == 'Letting_test_name'
