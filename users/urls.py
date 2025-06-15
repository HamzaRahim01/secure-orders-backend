from django.urls import path
from .views import UserList, UserRetrieveUpdateDestroy, RegisterCreate

app_name = 'users'
urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('register/', RegisterCreate.as_view(), name='register'),
]