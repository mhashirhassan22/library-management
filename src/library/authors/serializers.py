from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    total_books = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'biography', 'total_books', 'created_at', 'updated_at']
