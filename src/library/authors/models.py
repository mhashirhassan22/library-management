from django.db import models
from core.models import TimestampMixin
import uuid

# Create your models here.
class Author(TimestampMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def total_books(self):
        return self.books.count()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        indexes = [
            models.Index(fields=['first_name', 'last_name']),
        ]
