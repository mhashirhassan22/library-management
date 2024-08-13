from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserRegistrationTests(APITestCase):
    def test_user_registration(self):
        """
        Ensure we can create a new user with a username, email, password, and confirm password.
        """
        url = reverse('users:signup')
        data = {
            'email': 'user@test.com',
            'username': 'user123',
            'password': 'testpass123',
            'confirm_password': 'testpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'user@test.com')

    def test_user_registration_password_mismatch(self):
        """
        Ensure registration fails if password and confirm_password do not match.
        """
        url = reverse('users:signup')
        data = {
            'email': 'user@test.com',
            'username': 'user123',
            'password': 'testpass123',
            'confirm_password': 'mismatchpass'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

class UserLoginTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='user@test.com', password='testpass123', username='user123')

        self.user.is_active = True
        self.user.save()

    def test_user_login(self):
        """
        Ensure we can log in a user with an email and receive a token response.
        """
        url = reverse('users:token_obtain_pair')
        data = {'username': 'user123', 'password': 'testpass123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)
