from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Author
import uuid
from django.contrib.auth import get_user_model
User = get_user_model()

class AuthorAPITests(APITestCase):

    def setUp(self):
        # test user creation and login
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        response = self.client.post(reverse('users:token_obtain_pair'), {'username': 'testuser', 'password': 'testpassword'})
        self.token = response.data.get('access', None)
        self.assertIsNotNone(self.token, "Access token is missing in the response.")
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # test data
        self.author = Author.objects.create(
            name='John Doe',
            biography='Some biography'
        )

    def test_get_all_authors(self):
        url = reverse('author-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_author(self):
        url = reverse('author-detail', args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')

    def test_create_author(self):
        url = reverse('author-list-create')
        data = {
            'name': 'Jane Doe',
            'biography': 'Another biography',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)

    def test_update_author(self):
        url = reverse('author-detail', args=[self.author.id])
        data = {
            'name': 'John Smith',
            'biography': 'Updated biography',
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, 'John Smith')

    def test_delete_author(self):
        url = reverse('author-detail', args=[self.author.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 0)
