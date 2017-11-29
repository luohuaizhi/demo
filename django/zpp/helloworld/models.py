from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    birthday = models.DateField()
    gender = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
