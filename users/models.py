from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    # username = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    is_admin = models.BooleanField(default=False)
    test = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.id}, first name ({self.first_name}), last_name ({self.last_name})'


