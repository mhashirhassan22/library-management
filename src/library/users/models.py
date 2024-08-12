from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email Address', unique=True)

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.username
