from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Thing

# Create your tests here.
class ThingModelTestCase(TestCase):

    def setUp(self):
        self.thing = Thing.objects.create_user(
            name='@johndoe', 
            description='Hi, my name is John.',
            quantity =10
        )

    def test_assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')

    def test_assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()
