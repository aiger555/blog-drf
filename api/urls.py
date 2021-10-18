from django.urls import path
from .views import (
    UserListView, 
    UserDetailView,
    PostDetailView,
    PostListView,
)

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('posts/', PostListView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
]