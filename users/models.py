from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True, db_index=True)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)

def __str__(self):
    return self.email
