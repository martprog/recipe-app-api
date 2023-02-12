from django.contrib.auth import get_user_model
from django.test import TestCase

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = "email@example.com"
        password = "password123"
        user = get_user_model().objects.create_user(
                email=email, password=password
                )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normaliyed(self):
        sample_emails = [
            ['email1@EXAMPLE.com','email1@example.com'],
            ['Email2@Example.com','Email2@example.com'],
            ['EMAIL3@EXAMPLE.COM','EMAIL3@example.com'],
            ['email4@example.COM','email4@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'password123')
            self.assertEqual(user.email, expected)
