from rest_framework import serializers
from .models import Book, Favorite
from authors.models import Author

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    class Meta:
        model = Book
        depth = 1
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Favorite
        fields = ['id', 'book', 'added_at']

class AddFavoriteSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    class Meta:
        model = Favorite
        depth = 1
        fields = ['book']

    def create(self, validated_data):
        user = self.context['request'].user
        book = validated_data.get('book')
        favorite, created = Favorite.objects.get_or_create(user=user, book=book)
        return favorite

    def validate(self, data):
        user = self.context['request'].user
        # MAX 20 favorites allowed
        if Favorite.objects.filter(user=user).count() >= 20:
            raise serializers.ValidationError("You can't have more than 20 favorite books.")
        return data
