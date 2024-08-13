from django.db import models
from core.models import TimestampMixin
from authors.models import Author
import uuid
from django.contrib.auth import get_user_model
User = get_user_model()

class Book(TimestampMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    published_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True) # International Standard Book Number
    cover_image = models.URLField(blank=True, null=True)
    page_count = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

class Favorite(TimestampMixin, models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='favorited_by', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'book'], name='unique_favorite'),
        ]
        indexes = [
            models.Index(fields=['user', 'book']),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
