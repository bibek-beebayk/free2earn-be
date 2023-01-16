from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .base import TimeStampModel
from .managers import UserManager


class Skill(TimeStampModel):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class User(TimeStampModel, AbstractBaseUser, PermissionsMixin):

    USER_TYPE_CHOICES = [
        ('public', 'public'),
        ('refugee', 'refugee'),
        ('volunteer', 'volunteer'),
        ('manager', 'manager'),
        ('organization user', 'organization user'),

    ]

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=255, choices=USER_TYPE_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self) -> str:
        return self.username


class Refugee(User):
    is_skilled = models.BooleanField(default=False)
    skills = models.ManyToManyField(Skill, related_name='refugees')


class OrganizationUser(User):
    pass


class Manager(User):
    pass


class PublicUser(User):
    pass
