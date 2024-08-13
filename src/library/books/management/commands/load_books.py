import ijson
from django.core.management.base import BaseCommand
from books.models import Book
from authors.models import Author
from django.conf import settings
import os
from datetime import datetime

class Command(BaseCommand):
    help = 'Load Books into the database'

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'books.json'), 'r') as f:
            count = 0
            bulk = []
            for obj in ijson.items(f, '', multiple_values=True):
                for a in obj.get('authors', []):
                    author = Author.objects.get_or_create(id=int(a['id']), defaults={'name':a['name']})

                if obj.get('author_id', None):
                    author = Author.objects.get_or_create(id=int(obj['author_id']), defaults={'name':obj.get('author_name', 'None')})

                published_date_str = obj.get('publication_date')
                if published_date_str:
                    if len(published_date_str) == 7:  # Format: YYYY-MM
                        published_date = datetime.strptime(published_date_str, '%Y-%m')
                    elif len(published_date_str) > 7:  # Format: YYYY-MM-DD
                        published_date = datetime.strptime(published_date_str, '%Y-%m-%d')
                    else:
                        published_date = None
                else:
                    published_date = None
                processed_obj = {
                    'pk': int(obj.get('id')),
                    'title': obj.get('title'),
                    'description': obj.get('description'),
                    'author_id': int(obj.get('author_id')),
                    'published_date':published_date,
                    'isbn': obj.get('isbn'),
                    'cover_image': obj.get('image_url'),
                    'page_count': int(obj.get('num_pages')) if obj.get('num_pages') else None,
                    'language': obj.get('language'),
                }
                bulk.append(Book(**processed_obj))
                count += 1
                if count >= 50:
                    self.bulk_create_books(bulk)
                    bulk = []
                    count = 0

            self.bulk_create_books(bulk)


    def bulk_create_books(self, buffer):
        try:
            Book.objects.bulk_create(buffer)
        except:
            print("error creating books")
