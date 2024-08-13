from django.db import models
from core.models import TimestampMixin
import uuid

# Create your models here.
class Author(TimestampMixin, models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.name}"

    @property
    def total_books(self):
        return self.books.count()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
