from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models


class Admin(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('name', max_length=100)
    username = models.CharField('username', max_length=150, unique=True)
    email = models.EmailField('email address', unique=True)
    status = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    forgotStatus = models.BooleanField(default=True)
    class Meta:
        db_table = "admin"
        ordering = ('id',)
        
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.email)
