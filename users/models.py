from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    """User model without a username, using email for authorization."""

    username = None
    email = models.EmailField(unique=True, max_length=254, verbose_name='электронная почта')
    user_id_telegram = models.CharField(max_length=32, verbose_name='id пользователя в телеграм', **NULLABLE)

    # Additional fields
    phone = models.CharField(max_length=50, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: The email address of the object.
        """

        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
