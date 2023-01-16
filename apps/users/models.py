from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from be.libs.models import TimeStampModel


class BaseUser(TimeStampModel, AbstractBaseUser, PermissionsMixin):

    USER_TYPE_CHOICES = [
        ('public', 'public'),
        ('refugee', 'refugee'),
        ('volunteer', 'volunteer'),
        ('manager', 'manager'),
        ('organization user', 'organization user'),

    ]

    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=255, choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = 'username'




