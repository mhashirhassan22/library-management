from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),
    path('<uuid:id>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]
