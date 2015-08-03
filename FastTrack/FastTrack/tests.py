
from django.test import TestCase
from views import *
import unittest
from django.test.client import Client


from forms import MyForms
#from models import RegistrationProfile


class RegistrationTestCase(TestCase):
    """
    Base class for the test cases; this sets up two users -- one
    expired, one not -- which are used to exercise various parts of
    the application.

    """
    def setUp(self):
        self.sample_user = User.objects.create_user(username='alice', password='secret', first_name='a', last_name='b',
                                                                            email='alice@example.com')
        self.sample_user2 = User.objects.create_user(username='bob', password='secret', first_name='b', last_name='a',
                                                                            email='bob@example.com')

class RegistrationModelTests(RegistrationTestCase):
    """
    Tests for the model-oriented functionality of django-registration,
    including ``RegistrationProfile`` and its custom manager.

    """
    def test_registration_profile_created(self):
        """
        Test that a ``RegistrationProfile`` is created for a new user.

        """
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(self.sample_user.username, 'alice')
        self.assertEqual(self.sample_user.first_name, 'a')
        self.assertEqual(self.sample_user.last_name, 'b')
        self.assertEqual(self.sample_user.email, 'alice@example.com')

#test to make sure the created user successfully login
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.sample_user = User.objects.create_user(username='alice', password='secret', first_name='a', last_name='b',
                                                                            email='alice@example.com')
        self.client = Client()
        # login user
        login = self.client.login(username='alice', password='secret')
        # Check login
        self.assertEqual(login, True)

    def test_details(self):
        # get the home view
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


# self.assertEqual(login, True) --> login evals to False, raises the assertion
