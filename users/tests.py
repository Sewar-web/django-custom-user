from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CustomUser

class Userests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'sewar',
            email = 's.maqableh@yahoo.com',
            password = 'Sewar1997',
        )


    def test_create_newuser(self):

        self.assertEquals(self.user.username, 'sewar')
        self.assertEquals(self.user.email, 's.maqableh@yahoo.com')


    def test_duplicate_email(self):
        try:

            self.user2 = get_user_model().objects.create_user(
                username='sewar',
                email='s.maqableh@yahoo.com',
                password='Sewar1997'
            )

        except:
            print('This Email is Registered')