from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserRegistrationTests(APITestCase):
    def test_user_registration(self):
        """
        Ensure we can create a new user with an email as the main field.
        """
        url = reverse('users:signup')
        data = {'email': 'user@example.com', 'password': 'testpass123', 'username':'user123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'user@example.com')

class UserLoginTests(APITestCase):
    def setUp(self):
        # Create a user for testing login
        self.user = User.objects.create_user(email='user@example.com', password='testpass123', username='user123')

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
