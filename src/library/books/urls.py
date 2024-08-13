from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView, \
FavoriteListView, AddFavoriteView, RemoveFavoriteView, RecommendedBooksView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),
    path('<int:id>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),

    # favorites & recommendations
    path('favorites/', FavoriteListView.as_view(), name='favorite-list'),
    path('favorites/add/', AddFavoriteView.as_view(), name='add-favorite'),
    path('favorites/remove/<int:pk>/', RemoveFavoriteView.as_view(), name='remove-favorite'),
    path('recommendations/', RecommendedBooksView.as_view(), name='recommended-books'),
]
