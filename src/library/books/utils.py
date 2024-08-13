from django.db.models import Q
from .models import Book, Favorite

def get_recommended_books(user):
    favorite_books = Favorite.objects.filter(user=user).select_related('book')
    favorite_book_ids = [fav.book.id for fav in favorite_books]

    query = Q()
    for fav in favorite_books:
        query |= Q(author=fav.book.author) | Q(title__icontains=fav.book.title)

    similar_books = Book.objects.filter(query).exclude(id__in=favorite_book_ids).distinct()

    return similar_books[:5]
