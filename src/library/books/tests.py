from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from authors.models import Author  # Import the Author model
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()

class BookAPITests(APITestCase):

    def setUp(self):
        # test user creation and login
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        response = self.client.post(reverse('users:token_obtain_pair'), {'username': 'testuser', 'password': 'testpassword'})
        self.token = response.data.get('access', None)
        self.assertIsNotNone(self.token, "Access token is missing in the response.")
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # creating test data
        self.author = Author.objects.create(id=uuid.uuid4(), first_name='Hashir', last_name='Hassan')
        self.book1 = Book.objects.create(id=uuid.uuid4(), title='Python 101 By Hashir', author=self.author)
        self.book2 = Book.objects.create(id=uuid.uuid4(), title='Django Development', author=self.author)

    def test_get_all_books(self):
        url = reverse('book-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        url = reverse('book-list-create')
        data = {
            'title': 'New Book',
            'author': str(self.author.id),
            'description': 'A quick brown fox jumps over the lazy dog',
        }
        response = self.client.post(url, data, format='json')
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            print("Create Book Error:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        data = {
            'title': 'Updated Book',
            'author': str(self.author.id),
            'description': 'updating A quick brown dog jumps over the lazy fox',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_single_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Python 101 By Hashir')

    def test_search_books_by_title_case_insensitive(self):
        url = reverse('book-list-create')
        response = self.client.get(url, {'search': 'python'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Python 101 By Hashir')

    def test_search_books_by_author_case_insensitive(self):
        url = reverse('book-list-create')
        response = self.client.get(url, {'search': 'Hashir'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
