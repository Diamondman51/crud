from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save_password(self, password: str):
        if not password.startswith('pbkdf2_sha'):
            return super().set_password(password)
        return password

    def save(self, *args, **kwargs):
        self.save_password(self.password)
        return super().save(*args, **kwargs)
