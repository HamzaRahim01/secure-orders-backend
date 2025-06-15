from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy

app_name = 'users'
urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
]