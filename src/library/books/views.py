from rest_framework import generics, permissions, status
from .models import Book, Favorite
from rest_framework.response import Response
from django.db.models import Q
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from .serializers import FavoriteSerializer, AddFavoriteSerializer, BookSerializer
from .utils import get_recommended_books

@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(name='search', type=str, description='Search books by title or author name', required=False)
        ]
    ),
    post=extend_schema(
        parameters=[]  #Search param is not required for POST
    )
)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(author__first_name__icontains=search_query) |
                Q(author__last_name__icontains=search_query)
            )
        return queryset

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'put', 'delete'] # No need for PATCH as per requirements


class FavoriteListView(generics.ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

class AddFavoriteView(generics.CreateAPIView):
    serializer_class = AddFavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RemoveFavoriteView(generics.DestroyAPIView):
    serializer_class = AddFavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

class RecommendedBooksView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return get_recommended_books(user)
