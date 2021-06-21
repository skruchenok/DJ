from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class ToDo(models.Model):
    text = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:50]
