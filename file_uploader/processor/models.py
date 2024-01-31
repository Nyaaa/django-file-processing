from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class File(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.file)
