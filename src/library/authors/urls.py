from django.urls import path
from .views import AuthorListCreateView, AuthorRetrieveUpdateDestroyView

urlpatterns = [
    path('', AuthorListCreateView.as_view(), name='author-list-create'),
    path('<uuid:id>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),
]
